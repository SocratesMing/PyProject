# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.


def isPalindrome(s=""):
    l, r = 0, len(s) - 1
    s = s.lower()
    while l < r:
        while not s[l].isalpha() and l < r: #遇到非字符的就跳过
            l += 1
        while not s[r].isalpha() and l < r: #遇到非字符的就跳过
            r -= 1
        if s[r] != s[l]: #如果不符合就返回
            return False
        l += 1
        r -= 1
    else:
        return True


print(isPalindrome("A man, a plan, a canal: Panama"))
