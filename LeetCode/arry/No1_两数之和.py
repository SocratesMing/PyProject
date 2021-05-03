nums = [ 11, 15,2, 7]
target = 9

def twoSum(arr,target):
    mapDic = {}

    for x in range(len(arr)):
        sub = target-arr[x]
        if mapDic.get(arr[x])!=None:
            return x,mapDic[arr[x]]
        else:
            mapDic[sub]=x
        print(mapDic)


print(twoSum(nums,target))
