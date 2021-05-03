# Given nums = [0,0,1,1,1,2,2,3,3,4]
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.

def countArr(arr):
    n = len(arr)
    count = 0
    left, right = 0, 0
    while left <= right and right < n:
        if arr[left] == arr[right]:
            right += 1
        else:
            print(arr[left], arr[right])
            left = right
            count += 1  # 统计的是当前指针的前一个元素

    return count + 1  # 最后要把元素加上


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5]
print(countArr(arr))
