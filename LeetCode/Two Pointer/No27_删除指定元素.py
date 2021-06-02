# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums
# containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.


def removeElement(arr, ele):
    if len(arr) == 0:
        return 1
    j = 0  # j始终指向第一个要删除的元素

    for i in range(len(arr)):  # i始终指向当前元素
        print(arr)
        if arr[i] != ele:  # 与要删除的元素不相等

            if i != j:  # 两个索引不同
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
            print(i, j)

    return j


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

res = removeElement(nums, val)
print(res)
