

def findTarget(arr,target):
    map = {}
    res = []
    for v in arr:
        if map.get(v)!=None:
            res.append([v,map[v]])
        else:
            map[target-v]=v

    return  res
arr = [1,2,3,4,5,6]
print(findTarget(arr,7))
