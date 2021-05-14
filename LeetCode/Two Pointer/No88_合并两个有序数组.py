# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

def mergeArr(num1, m, num2, n):
    id1 = m - 1
    id2 = n - 1
    k = m + n - 1
    while id1 >= 0 and id2 >= 0:
        print(id1,id2,k)
        if num2[id2] > num1[id1]:
            num1[k] = num2[id2]
            id2 -= 1
        else:
            num1[k] = num1[id1]
            id1 -= 1
        k -= 1
        print(num1)
    return num1


print(mergeArr([1, 2, 3, 0, 0, 0], 3, [2, 5, 6],3))
