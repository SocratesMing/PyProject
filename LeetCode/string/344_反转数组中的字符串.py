# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# 思路：对撞指针

def reverseStr(strArr):
    l, r = 0, len(strArr) - 1

    while r < l:
        strArr[l], strArr[r] = strArr[r], strArr[l],
        r -= 1
        l += 1
    return strArr
def reverseStr2(strArr):
    return strArr[::-1] #直接调用内置函数
print(reverseStr2(["H", "a", "n", "n", "a", "h"]))
