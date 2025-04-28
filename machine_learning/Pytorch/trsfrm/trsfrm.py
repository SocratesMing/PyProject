import math

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader
import uuid


# 自定义数据集
class TimeSeriesDataset(Dataset):
    def __init__(self, data, seq_length):
        self.data = data
        self.seq_length = seq_length

    def __len__(self):
        return len(self.data) - self.seq_length

    def __getitem__(self, index):
        x = self.data[index:index + self.seq_length]
        y = self.data[index + self.seq_length, 3]  # 预测收盘价（索引3）
        return torch.FloatTensor(x), torch.FloatTensor([y])


# Transformer模型
class TransformerModel(nn.Module):
    def __init__(self, input_size=4, d_model=64, nhead=4, num_layers=2, dropout=0.2):
        super(TransformerModel, self).__init__()
        self.input_linear = nn.Linear(input_size, d_model)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dropout=dropout, batch_first=True),
            num_layers=num_layers
        )
        self.fc = nn.Linear(d_model, 1)

    def forward(self, x):
        x = self.input_linear(x)  # 将输入映射到d_model维度
        x = self.transformer(x)  # Transformer编码
        out = self.fc(x[:, -1, :])  # 取最后一个时间步的输出
        return out

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=1000):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer("pe", pe)

    def forward(self, x):
        # [T, N, F]
        return x + self.pe[: x.size(0), :]

class Transformer(nn.Module):
    def __init__(self, d_feat=6, d_model=8, nhead=4, num_layers=2, dropout=0.5, device=None):
        super(Transformer, self).__init__()
        self.feature_layer = nn.Linear(d_feat, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.decoder_layer = nn.Linear(d_model, 1)
        self.device = device
        self.d_feat = d_feat

    def forward(self, src):
        # src [N, T, F], [512, 60, 6]
        src = self.feature_layer(src)  # [512, 60, 8]

        # src [N, T, F] --> [T, N, F], [60, 512, 8]
        src = src.transpose(1, 0)  # not batch first

        mask = None

        src = self.pos_encoder(src)
        output = self.transformer_encoder(src, mask)  # [60, 512, 8]

        # [T, N, F] --> [N, T*F]
        output = self.decoder_layer(output.transpose(1, 0)[:, -1, :])  # [512, 1]

        return output.squeeze()


# 数据预处理
def preprocess_data(file_path, seq_length=10):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 假设CSV包含'Date', 'Open', 'High', 'Low', 'Close'列
    features = df[['open', 'high', 'low', 'close']].values

    # 归一化
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    # 创建数据集
    dataset = TimeSeriesDataset(scaled_data, seq_length)
    train_size = int(len(dataset) * 0.8)
    train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, len(dataset) - train_size])

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    return train_loader, test_loader, scaler, scaled_data.shape[1]


# 训练模型
def train_model(model, train_loader, criterion, optimizer, num_epochs=50):
    model.train()
    for epoch in range(num_epochs):
        total_loss = 0
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            output = model(batch_x)
            loss = criterion(output, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {total_loss / len(train_loader):.6f}')


# 测试模型
def test_model(model, test_loader, criterion):
    model.eval()
    total_loss = 0
    predictions, actuals = [], []
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            output = model(batch_x)
            loss = criterion(output, batch_y)
            total_loss += loss.item()
            predictions.extend(output.numpy().flatten())
            actuals.extend(batch_y.numpy().flatten())
    print(f'Test Loss: {total_loss / len(test_loader):.6f}')
    return predictions, actuals


# 主函数
def main(file_path):
    # 参数设置
    seq_length = 10
    input_size = 4  # OHLC四个特征
    d_model = 64
    nhead = 4
    num_layers = 2
    num_epochs = 50
    learning_rate = 0.001

    # 数据预处理
    train_loader, test_loader, scaler, input_size = preprocess_data(file_path, seq_length)

    # 初始化模型
    model = TransformerModel(input_size, d_model, nhead, num_layers)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # 训练模型
    train_model(model, train_loader, criterion, optimizer, num_epochs)

    # 测试模型
    predictions, actuals = test_model(model, test_loader, criterion)

    # 反归一化预测结果
    predictions = np.array(predictions).reshape(-1, 1)
    actuals = np.array(actuals).reshape(-1, 1)

    # 创建一个四列的数组，用于反归一化（只关心收盘价）
    dummy = np.zeros((len(predictions), 4))
    dummy[:, 3] = predictions[:, 0]
    predictions = scaler.inverse_transform(dummy)[:, 3]

    dummy[:, 3] = actuals[:, 0]
    actuals = scaler.inverse_transform(dummy)[:, 3]

    # 保存预测结果
    results = pd.DataFrame({
        'Actual': actuals,
        'Predicted': predictions
    })
    results.to_csv('transformer_predictions.csv', index=False)
    print("Predictions saved to 'transformer_predictions.csv'")


if __name__ == "__main__":
    # 替换为你的CSV文件路径
    file_path = "../data/USDCNHSP.csv"
    main(file_path)