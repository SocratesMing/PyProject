# Input: 120
# Output: 21

# NOTE:这种算法只适用于正整数，由于python对负数取余数是向负无穷取数，因此得到的一般是正数。
def reverseNum(num):

    res = 0
    while num != 0:
        res = res*10+num%10
        num = num //10
    print(res)
    if res > 1>>31-1 or -(1<<31):
        return 0
    else:
        return res

print(reverseNum(120))