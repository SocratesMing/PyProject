# Input:
# matrix = [
# [1, 3, 5, 7],
# [10, 11, 16, 20],
# [23, 30, 34, 50]
# ]
# target = 3
# Output: true

def searchMatrix(Matrix, target):
    ml = len(Matrix)

    if ml == 0:
        return False

    m, low, high = len(Matrix[0]), 0, len(Matrix[0]) * ml
    while low <= high:
        mid = low + ((high - low) >> 1)
        print(mid // m,mid % m)
        if Matrix[mid // m][mid % m] == target:
            return True
        elif Matrix[mid // m][mid % m] > target:
            high = mid - 1
        else:
            low = mid + 1


Matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

print(searchMatrix(Matrix, 1))
