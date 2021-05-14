# 判断⼀个整数是否是回⽂数。回⽂数是指正序（从左向右）和倒序（从右向左）读都是⼀样的整数。

def isPalindrome(num):
    if num > 10:
        num = str(num)
        l = len(num)
        for x in range(l>>1):
            if num[x]!= num[l-1-x]:
                return False
        return True

    elif num ==0:
        return 0

    else:
        return False

print(isPalindrome(1213))