# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def maxSaveWater(arr):
    res, left, right, leftMax, rightMax = 0, 0, len(arr) - 1, arr[0], arr[-1]

    while left <= right:
        if arr[left] < arr[right]:
            if arr[left] < leftMax:
                res += leftMax - arr[left]
            else:
                leftMax = arr[left]
            left += 1
        else:
            if arr[right] < rightMax:
                res += rightMax - arr[right]
            else:
                rightMax = arr[right]
            right -= 1
    return res


print(maxSaveWater(nums))
