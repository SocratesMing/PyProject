# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2,

def findPeakElement1(arr):
    """ 二分法不太对"""
    left,right = 0,len(arr)-1

    while left<right:
        mid = left+(right-left)>>1
        if arr[mid]>arr[mid+1]:
            right = mid
        else:
            left=mid+1
    return left

def findPeakElement2(arr):
    res = []
    for x in range(1,len(arr)-1,):
        if arr[x]>arr[x-1] and arr[x]>arr[x+1]:
            res.append(x)
    print(res)
arr = [1,2,1,3,5,6,4]
# print(findPeakElement1(arr))
print(findPeakElement2(arr))
