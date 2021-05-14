nums = [11, 15, 2, 7]
target = 9


def twoSum(arr, target):
    mapDic = {}

    for x in range(len(arr)):
        sub = target - arr[x]
        if mapDic.get(arr[x]) != None:  # 如果取出来了就返回（当前索引和余数对应的索引）
            return x, mapDic[arr[x]]
        else:
            mapDic[sub] = x  # 添加余数和对应的索引
        print(mapDic)


print(twoSum(nums, target))
