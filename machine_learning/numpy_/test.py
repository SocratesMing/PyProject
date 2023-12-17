import numpy as np

X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
print(np.arange(1, 11))
print(np.arange(0, 10))
print(np.arange(0, 10)[:, np.newaxis])
# print(np.arange(0, 10)[:, np.newaxis][:, np.newaxis])
print(np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])