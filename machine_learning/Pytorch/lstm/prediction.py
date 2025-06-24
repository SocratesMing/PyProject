import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from loguru import logger
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader

logger.add("lstm.log", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")


# 自定义数据集
class TimeSeriesDataset(Dataset):
    def __init__(self, data, seq_length):
        self.data = data
        self.seq_length = seq_length

    def __len__(self):
        return len(self.data) - self.seq_length

    def __getitem__(self, index):
        x = self.data[index:index + self.seq_length]
        y = self.data[index + self.seq_length, -1]  # 预测收盘价（索引最后一列）
        # x_tensor, y_tensor = torch.FloatTensor(x), torch.FloatTensor([y])
        # print("数据集中是否含有 nan {} 数据集中是否含有 nan {} ", torch.isnan(x_tensor).any(), y_tensor)

        # return x_tensor, y_tensor
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
        logger.info(
            f"模型参数为 d_feat:{d_feat}, hidden_size:{hidden_size}, num_layers:{num_layers}, dropout:{dropout}")
        self.fc_out = nn.Linear(hidden_size, 1)

        self.d_feat = d_feat

    def forward(self, x):
        # print("x - ",x.shape)
        out, _ = self.rnn(x)
        # print("out - ",out.shape)
        # return self.fc_out(out[:, -1, :]).squeeze()
        return self.fc_out(out[:, -1, :])


# 数据预处理
def preprocess_data(file_path, seq_length=10, batch_size=64):
    # 读取CSV文件
    logger.info("读取文件 {}", file_path)
    df = pd.read_csv(file_path)
    # df = df.iloc[::200]
    if df.isna().any().any():
        df = df.dropna()
        logger.info("清除掉df中的na值 ")
    logger.info("df中的含na值 {}", df.isna().any().any())
    logger.info("df.shape  {}", df.shape)

    # 假设CSV包含'Date', 'Open', 'High', 'Low', 'Close'列

    # features = df[['open', 'high', 'low', 'close']].values
    logger.info("特征为:{}", df.columns.tolist())
    features = df[df.columns].values
    # print("features.shape", features.shape)
    # print("features.data", features)

    # 归一化
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    # 创建数据集
    dataset = TimeSeriesDataset(scaled_data, seq_length)

    train_size = int(len(dataset) * 0.7)
    # train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, len(dataset) - train_size])
    train_indices = list(range(0, train_size))
    val_indices = list(range(train_size, len(dataset)))
    train_dataset = torch.utils.data.Subset(dataset, train_indices)
    test_dataset = torch.utils.data.Subset(dataset, val_indices)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader, scaler, scaled_data.shape[1]


# 训练模型
def train_model(device, model, train_loader, criterion, optimizer, num_epochs=10):
    model.train()
    for epoch in range(num_epochs):
        total_loss = 0
        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            optimizer.zero_grad()
            output = model(batch_x)
            loss = criterion(output, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if (epoch + 1) % 10 == 0:
            logger.info(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {total_loss / len(train_loader):.6f}')


# 测试模型
def test_model(device, model, test_loader, criterion):
    model.eval()
    total_loss = 0
    predictions, actuals = [], []
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            output = model(batch_x)
            loss = criterion(output, batch_y)
            total_loss += loss.item()
            predictions.extend(output.cpu().numpy().flatten())
            actuals.extend(batch_y.cpu().numpy().flatten())
    logger.info(f'Test Loss: {total_loss / len(test_loader):.6f}')
    return predictions, actuals


def cal_res():
    # 读取CSV文件（假设列名为"Actual"和"Predicted"）
    df = pd.read_csv("predictions.csv")
    # print(df.head())
    # 生成前一行数据列（通过shift(1)获取）
    df["前一行_Actual"] = df["Actual"].shift(1)
    df["前一行_Predicted"] = df["Predicted"].shift(1)

    # 删除首行空值
    df = df.dropna(subset=["前一行_Actual", "前一行_Predicted"])

    # 判断条件：
    # 情况1：Actual当前行 > 前一行，且Predicted当前行 > 前一行
    condition_up = (df["Actual"] >= df["前一行_Actual"]) & (df["Predicted"] >= df["前一行_Actual"])

    # 情况2：Actual当前行 < 前一行，且Predicted当前行 < 前一行
    condition_down = (df["Actual"] <= df["前一行_Actual"]) & (df["Predicted"] <= df["前一行_Actual"])

    # 统计符合条件的总行数
    correct_counts = (condition_up | condition_down).sum()

    # 计算准确率（排除首行后的总比较次数）
    total_comparisons = len(df)
    accuracy = correct_counts / total_comparisons

    print(f"预测方向准确率: {accuracy:.2%}")
    logger.info(f"预测方向准确率: {accuracy:.2%}")


# 主函数
def main(file_path):
    # 参数设置
    seq_length = 48
    hidden_size = 5
    num_layers = 5
    num_epochs = 100
    learning_rate = 0.01
    batch_size = 48
    dropout = 0.0
    logger.info(
        "seq_length:{} hidden_size:{} num_layers:{} num_epochs:{} learning_rate:{} batch_size:{} dropout:{}",
        seq_length, hidden_size, num_layers, num_epochs, learning_rate, batch_size, dropout)
    # 数据预处理
    train_loader, test_loader, scaler, input_size = preprocess_data(file_path, seq_length, batch_size)

    # sys.exit()
    logger.info("训练集数据 {}, 测试集数据 {}", len(train_loader), len(test_loader))
    logger.info("开始训练模型")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("训练设备为 {}", device)
    # 初始化模型
    model = LSTMModel(input_size, hidden_size, num_layers, dropout=dropout).to(device)
    logger.info("模型参数 {}", model.parameters())

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    # 训练模型
    train_model(device, model, train_loader, criterion, optimizer, num_epochs)

    # 测试模型
    logger.info("开始测试模型")
    predictions, actuals = test_model(device, model, test_loader, criterion)

    # 反归一化预测结果
    predictions = np.array(predictions).reshape(-1, 1)
    actuals = np.array(actuals).reshape(-1, 1)
    # print("predictions", predictions, type(predictions), len(predictions[0]))
    # print("actuals", actuals, type(predictions), len(actuals[0]))

    # 创建一个四列的数组，用于反归一化（只关心收盘价）
    dim = input_size
    last_ind = dim - 1
    dummy = np.zeros((len(predictions), dim))
    dummy[:, last_ind] = predictions[:, 0]
    predictions = scaler.inverse_transform(dummy)[:, last_ind]

    dummy[:, last_ind] = actuals[:, 0]
    actuals = scaler.inverse_transform(dummy)[:, last_ind]

    # 保存预测结果
    results = pd.DataFrame({
        'Actual': actuals,
        'Predicted': predictions
    })
    results.to_csv(f'predictions.csv', index=False)
    logger.info("Predictions saved to 'predictions.csv'")
    cal_res()


if __name__ == "__main__":
    # 替换为你的CSV文件路径
    # file_path = "../data/USDCNHSP.csv"
    # file_path = "./eur-22-24-5m_MA[5_10_20].csv"
    # file_path = "./eur-22-24-5m_10.csv"
    file_path = r"D:\Code\Python\PyProject\Quant\data\eur_h.csv"
    try:
        main(file_path)
    except Exception as e:
        logger.error(e)
