import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# 1. 数据加载和预处理
def load_and_preprocess_data(file_path, sequence_length=10):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 假设CSV包含日期和OHLC列，选择close价格
    data = df[['close']].values

    # 归一化数据
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # 创建序列数据
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])

    X = np.array(X)
    y = np.array(y)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 转换为PyTorch张量
    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)
    y_train = torch.FloatTensor(y_train)
    y_test = torch.FloatTensor(y_test)

    return X_train, X_test, y_train, y_test, scaler


# 2. 定义LSTM模型
class LSTMModel(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, num_layers=2, dropout=0.2):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        # 初始化隐藏状态
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        # LSTM前向传播
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])  # 取最后一个时间步的输出
        return out


# 3. 训练模型
def train_model(model, X_train, y_train, X_test, y_test, epochs=100, batch_size=32):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    X_train, y_train = X_train.to(device), y_train.to(device)
    X_test, y_test = X_test.to(device), y_test.to(device)

    # 训练循环
    for epoch in range(epochs):
        model.train()
        for i in range(0, len(X_train), batch_size):
            batch_X = X_train[i:i + batch_size]
            batch_y = y_train[i:i + batch_size]

            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 每10个epoch打印损失
        if (epoch + 1) % 10 == 0:
            model.eval()
            with torch.no_grad():
                test_outputs = model(X_test)
                test_loss = criterion(test_outputs, y_test)
            print(f'Epoch [{epoch + 1}/{epochs}], Train Loss: {loss.item():.6f}, Test Loss: {test_loss.item():.6f}')

    return model


# 4. 预测函数
def predict(model, X, scaler, device="cpu"):
    model.eval()
    X = torch.FloatTensor(X).to(device)
    with torch.no_grad():
        pred = model(X)
    pred = scaler.inverse_transform(pred.cpu().numpy())
    return pred


# 5. 主函数
def main():
    # 加载数据
    file_path = 'data/USDCNHSP.csv'  # 替换为你的CSV文件路径
    sequence_length = 10
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(file_path, sequence_length)

    # 初始化模型
    model = LSTMModel(input_size=1, hidden_size=50, num_layers=2, dropout=0.2)

    # 训练模型
    model = train_model(model, X_train, y_train, X_test, y_test, epochs=100, batch_size=32)

    # 预测
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    predictions = predict(model, X_test, scaler, device)

    # 可视化结果
    y_test_transformed = scaler.inverse_transform(y_test.cpu().numpy())
    plt.plot(y_test_transformed, label='Actual')
    plt.plot(predictions, label='Predicted')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()