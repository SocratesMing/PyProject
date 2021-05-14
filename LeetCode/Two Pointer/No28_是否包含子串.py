# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
# # haystack.


# Input: haystack = "hello", needle = "ll"
# Output: 2


def implementstr1(haystack, needle):
    for a in range(len(haystack)):
        for b in range(len(needle)):
            print(a, b)
            if b == len(needle) - 1 and haystack[a + b] == needle[b]:  # 第二个条件主要是为了一个元素查找不出错
                return a
            if a + b >= len(haystack)-1:  #应该是大于等于
                return -1
            if needle[b] != haystack[a + b]:
                break


haystack = "hello"
needle = "l"
print(implementstr1(haystack, needle))
