# Given nums = [0,0,1,1,1,2,2,3,3,4]
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.

def countArr(arr):
    n = len(arr)
    last, find = 0, 0
    while find < n-1:
        while arr[last] == arr[find]:#遇到相同的数就跳过
            find += 1
            if find==n-1:
                return last+1
        # 退出循环时find与当前last值不同
        arr[last+1]=arr[find]
        last +=1
    return last + 1  # 最后要把元素加上


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5]
print(countArr(arr))
