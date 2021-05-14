# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# [1, 7],
# [1, 2, 5],
# [2, 6],
# [1, 1, 6]
# ]

res = []


def combinationSum(num, target):
    if len(num) == 0:
        return []
    count = []
    num.sort()
    findCombination(num, target, 0, count)
    return res


def findCombination(num, target, index, count):
    print(target, index, count)

    if target == 0:
        res.append(count.copy())
        return

    for i in range(index, len(num)):
        if i > index and num[i] == num[index]:  # 剪枝优化，如果剩余元素比余值还大肯定组合不了，跳过
            continue
        if target >= num[i]:
            count.append(num[i])
            findCombination(num, target - num[i], i + 1, count)  # 注意这⾥迭代的时候 index 依旧不变，因为⼀个元素可以取多次
            count.pop()  # 返回了的话就要把上一次的元素pop出去
            print(count, target, i)


print(combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
