import torch
from torch.utils.data import Dataset, DataLoader


class TimeSeriesDataset(Dataset):
    def __init__(self, data, seq_length):
        self.data = torch.randn(data, 5)
        self.seq_length = seq_length

    def __len__(self):
        return len(self.data) - self.seq_length

    def __getitem__(self, index):
        x = self.data[index:index + self.seq_length]
        y = self.data[index + self.seq_length, -1]  # 预测收盘价（索引最后一列）
        return torch.FloatTensor(x), torch.FloatTensor([y])


test_dataset = TimeSeriesDataset(100, 4)
print("test_dataset", len(test_dataset))
for x in range(3):
    print(f"索引{x} \n", test_dataset[x])
print(" -- " * 5)
test_loader = DataLoader(test_dataset, batch_size=7, shuffle=False)  # 每个批次6个数据，总共 96/6 16个批次
print("test_loader ", len(test_loader))
i = 0
for x, y in test_loader:
    print(len(x), x)
