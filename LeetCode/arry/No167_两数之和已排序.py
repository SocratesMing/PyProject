# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

def twoSum(arr,target):  #双指针算法

    left,right = 0,len(arr)-1
    while left<right:
        if arr[left] + arr[right]==target:
            return left,right
        elif arr[left] + arr[right]>target:
            right-=1
        else:
            left+=1

arr = [2,7,11,15]

print(twoSum(arr,26))
