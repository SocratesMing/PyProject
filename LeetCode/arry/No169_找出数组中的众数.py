# Input: [2,2,1,1,1,2,2]
# Output: 2
""" 需要理解算法"""

def findMore(arr):

    res,count = arr[0],0
    for x in range(len(arr)):
        if count ==0:
            res,count = arr[x],1
        else:
            if arr[x]==res:
                count+=1
            else:
                count-=1

        print(res,count)
    print(res)
arr = [3,4,1,1,1,2,2,2,2,2,2,2,6,9,2,2]
arr = [2,1,2,3,2,1,2,3,2,1,2,3,2,2]

findMore(arr)