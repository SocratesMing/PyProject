# Input: [1,2,0]
# Output: 3
# Input: [3,4,-1,1]
# Output: 2
# Input: [7,8,9,11,12]
# Output: 1

def findFirstMissPos(num):
    map = {}
    for x in num:
        map[x] = x

    for i in range(1, len(num) + 1): #//从一开始
        if map.get(i) == None:
            return i
        else:
            print(map[i])


num = [7, 8, 9, 11, 12]
print(findFirstMissPos(num))
