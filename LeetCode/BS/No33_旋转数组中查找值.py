# nput: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def findValue(num, target):
    low, high = 0, len(num) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        print(low, high, mid)
        if num[mid] == target:
            return mid

        elif num[mid] > num[low]:  # 在前半区间
            if target >= num[low] and target < num[mid]:  # 两边的边界可以相等
                high = mid - 1
            else:
                low = mid + 1

        elif num[mid] < num[high]:  # 在后半区间
            if target > num[mid] and target <= num[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if num[mid] == num[low]:
                low += 1
            if num[mid] == num[high]:
                high -= 1

    return -1


def findValue2(num, target):
    low, high = 0, len(num) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        print(low, high, mid)
        if num[mid] == target:
            return mid

        if target >= num[low] and target <= num[mid]:  # 要与>=号
            high = mid - 1
        else:
            low = mid + 1

        if num[mid] == num[low]:
            low += 1
        if num[mid] == num[high]:
            high -= 1

    return -1


print(findValue2([4, 5, 6, 7, 0, 1, 2], 7))
