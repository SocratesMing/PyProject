# Input: nums = [1,2,3]
# Output:
# [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]

res = []


def permute(num):
    if len(num) == 0:
        return []
    if len(num) == 1:
        return [num, []]

    count = []
    for k in range(1, len(num)):
        generatePermuta(num, k, 0, count)
    res.append([])
    return res


def generatePermuta(num, k, index, count):
    if len(count) == k:
        res.append(count.copy())
        return
    for i in range(index, (len(num)) - (k - len(count)) + 1):  # num是因为index 从0开始，最后在+1是range不取最后一个数
        count.append(num[i])
        generatePermuta(num, k, i + 1, count)
        count.pop()
    return

print(permute([1, 2, 3]))
