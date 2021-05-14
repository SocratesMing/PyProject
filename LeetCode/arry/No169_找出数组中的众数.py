# iven an array of size n, find the majority element. The majority element is the element that
# appears more than ⌊n/2 ⌋times.
# Input: [2,2,1,1,1,2,2]
# Output: 2
""" 题目中要求的众数是大于一半以上，依次可以使用计数得方法"""


def findMore(arr):  #

    res, count = arr[0], 0
    for x in range(len(arr)):
        if count == 0:  # 根据count来计算
            res, count = arr[x], 1
        else:
            if arr[x] == res:
                count += 1
            else:
                count -= 1

        print(res, count)
    print(res)


# arr = [3,4,1,1,1,2,2,2,2,2,2,2,6,9,2,2]
# arr = [2,1,2,3,2,1,2,3,2,1,2,3,2,2]
arr = [2, 2, 2, 2, 1, 1, 1]

findMore(arr)
