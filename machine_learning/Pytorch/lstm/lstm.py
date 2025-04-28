import sys

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader
from loguru import logger

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



# LSTM模型
# class LSTMModel(nn.Module):
#     def __init__(self, input_size=4, hidden_size=64, num_layers=2, dropout=0.2):
#         super(LSTMModel, self).__init__()
#         self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=dropout)
#         self.fc = nn.Linear(hidden_size, 1)
#
#     def forward(self, x):
#         out, _ = self.lstm(x)
#         out = self.fc(out[:, -1, :])  # 取最后一个时间步的输出
#         return out

class LSTMModel(nn.Module):
    def __init__(self, d_feat=6, hidden_size=64, num_layers=2, dropout=0.0):
        super().__init__()

        self.rnn = nn.LSTM(
            input_size=d_feat,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout,
        )
        self.fc_out = nn.Linear(hidden_size, 1)

        self.d_feat = d_feat

    def forward(self, x):
        # print("x - ",x.shape)
        out, _ = self.rnn(x)
        # print("out - ",out.shape)
        # return self.fc_out(out[:, -1, :]).squeeze()
        return self.fc_out(out[:, -1, :])

# 数据预处理
def preprocess_data(file_path, seq_length=10):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    print("source data", df)

    # 假设CSV包含'Date', 'Open', 'High', 'Low', 'Close'列
    features = df[['open', 'high', 'low', 'close']].values
    print("features.shape", features.shape)
    print("features.data", features)

    # 归一化
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    # 创建数据集
    dataset = TimeSeriesDataset(scaled_data, seq_length)
    print(dataset, dataset.__len__())
    i = 1
    for x in dataset:
        print(x)
        if i == 5: break
        i += 1
    train_size = int(len(dataset) * 0.8)
    # train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, len(dataset) - train_size])
    train_indices = list(range(0, train_size))
    val_indices = list(range(train_size, len(dataset)))
    train_dataset = torch.utils.data.Subset(dataset, train_indices)
    test_dataset = torch.utils.data.Subset(dataset, val_indices)
    print("train size", len(train_dataset), "data", train_dataset.__getitem__(0))
    print("test size", len(test_dataset), "data", test_dataset.__getitem__(0))
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
    hidden_size = 64
    num_layers = 2
    num_epochs = 50
    learning_rate = 0.001

    # 数据预处理
    train_loader, test_loader, scaler, input_size = preprocess_data(file_path, seq_length)
    # sys.exit()

    # 初始化模型
    model = LSTMModel(input_size, hidden_size, num_layers)
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
    results.to_csv('predictions.csv', index=False)
    print("Predictions saved to 'predictions.csv'")


if __name__ == "__main__":
    # 替换为你的CSV文件路径
    file_path = "../data/USDCNHSP.csv"
    main(file_path)
