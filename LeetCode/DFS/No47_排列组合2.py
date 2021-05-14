# Input: [1,1,2]
# Output:
# [
# [1,1,2],
# [1,2,1],
# [2,1,1]
# ]


res = []


def permute(num):
    if len(num) == 0:
        return [[]]
    used, count = [False] * 3, []  # 用了一个标志位很巧妙
    generatePermuta(num, 0, count, used)
    return res


def generatePermuta(num, index, count, used):
    if index == len(num):
        print(count)
        res.append(count.copy())
        return
    for i in range(len(num)):
        if not used[i]:
            if i > 0 and num[i] == num[i - 1] and (not used[i - 1]):
                continue
            else:
                used[i] = True
                count.append(num[i])
                generatePermuta(num, index + 1, count, used)
                count.pop()
                used[i] = False

    return


print(permute([1, 1, 2]))
