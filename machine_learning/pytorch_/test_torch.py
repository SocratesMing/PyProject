# import torch
# from torch import nn
#
# loss = nn.MSELoss()
# input = torch.randn(3, 5, requires_grad=True)
# target = torch.randn(3, 5)
# print("input",input)
# print("target",target)
# output = loss(input, target)
# print(output)
# print(output.backward())  #计算梯度
import numpy as np
import torch

# 模拟数据 (batch_size=2, seq_len=3, input_dim=4)
# xx=torch.randn(4)
# print(xx)
# print(xx[0:-1])
# print(torch.randn( 3, 4))
# data = torch.randn(2, 3, 4)
# print(data)
# # 提取特征和标签
# feature = data[:, :, 0:-1]  # 形状: (2, 3, 3)
# label = data[:, -1, -1]     # 形状: (2,)
#
# print("Feature: ", feature);
# print("Label: ", label)


xx=torch.randn(3, 4)
print(xx)
print(xx[1:2,[2]])
print(xx[1:2,[2,3]])
print(xx[1:2,[1,3]])
print(torch.tensor([[[1, 2, 3]]]).squeeze())
a = np.array([[[1, 2, 3]]])  # 形状 (1, 1, 3)
b = np.squeeze(a)            # 形状 (3,)
print(b)
print(b.shape)               # 输出: (3,)