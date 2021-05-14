# Input: n = 4, k = 2
# Output:
# [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
# 给定两个整数n 和k，返回1 ... n 中所有可能的k 个数的组合。

res = []


def permute(n, k):
    if n < k or k == 0 or n <= 0:
        return []
    count = []
    generatePermuta(n, k, 1, count)
    return res


def generatePermuta(num, k, index, count):
    if len(count) == k:
        # print(count)
        res.append(count.copy())
        return
    for i in range(index, (num + 1) - (k - len(count)) + 1):  # num+1 是因为index 从1开始，最后在+1是range不取最后一个数

        count.append(i)
        generatePermuta(num, k, i + 1, count)
        count.pop()
    return


print(permute(6, 2))
