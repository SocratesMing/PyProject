# Input: [1,3,5,6], 5
# Output: 2

def findInsert(num, target):
    print("findInsert")
    low, high = 0, len(num) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        # print(mid, low, high)
        if target <= num[mid]:
            if mid == 0: #如果在左边界
                return mid
            high = mid - 1
        else:
            if mid == len(num) - 1 or num[mid + 1] >= target:#如果在右边界
                return mid + 1
            low = mid + 1


print(findInsert([1, 3, 5, 6], 5))
print(findInsert([1, 3, 5, 6], 7))
print(findInsert([0, 3, 5, 6], 0))
