nums = [-1, 0, 1, 2, -1, -4]
#双指针

def threeSum(arr=[]):
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n - 2):
        if arr[i] > 0:
            break
        if arr[i] == arr[i - 1]: continue
        left, right = i + 1, n - 1
        while left < right:
            target = arr[i] + arr[left] + arr[right]

            if target > 0:
                right -= 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif target < 0:
                left += 1
                while left < right and arr[left - 1] == arr[left]:
                    left += 1
            else:
                res.append([arr[i], arr[left], arr[right]])
                right -= 1
                left += 1
                while left < right and arr[left - 1] == arr[left]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
    return res


print(threeSum(nums))
