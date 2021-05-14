# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2,
# 题意输出其中一个峰值就好
def findPeakElement1(arr):
    """ 二分法不太对"""
    low, high = 0, len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)
        print(arr[low:high + 1])

        if arr[mid] > arr[mid + 1]:  # 根据二分后的最终结果，峰值满足[low,mid,high],mid >low and mid>high
            high = mid
        else:
            low = mid + 1
    return low  # 或者返回high


def findPeakElement2(arr):  # 直接根据题意来计算
    res = []
    for x in range(1, len(arr) - 1):
        if arr[x] > arr[x - 1] and arr[x] > arr[x + 1]:
            res.append(x)
    print(res)


arr = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement1(arr))
# print(findPeakElement2(arr))
