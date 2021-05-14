# Input: "leetcode"
# Output: "leotcede"

# 思路：对撞指针

def reverseStr(s):
    strArr = list(s)
    aoArr = ['a','o','i','u','e','A','O','I','U','E']
    l, r = 0, len(strArr) - 1

    while l < r:
        if strArr[l] in aoArr and strArr[r] in aoArr:
            strArr[l], strArr[r] = strArr[r], strArr[l]
            r -= 1
            l += 1
        elif  strArr[l] not in aoArr and strArr[r] in aoArr:
            l += 1
        elif  strArr[l] in aoArr and strArr[r] not in aoArr:
            r -= 1
        else:
            r -= 1
            l += 1
    # print(strArr)
    return "".join(strArr)

print(reverseStr("leetcode"))
