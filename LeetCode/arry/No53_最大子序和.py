# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArry1(num):  # 不用动态规划算法
    ind, res, maxlen = 0, 0, num[0],

    while ind < len(num):  # 依次相加，比最大值大就替换，如果和小于0就置为0，对于小于0的值只有最大值
        res += num[ind]
        if res > maxlen:
            maxlen = res
        if res < 0:
            res = 0
        ind += 1
    return maxlen


def maxSubArry2(num):  # 用动态规划算法

    nl = len(num)
    if nl == 0:
        return 0
    if nl == 1:
        return num[0]
    dp, res = [0] * nl, num[0]  # dp数组中记录的是当前序列的最大子序和

    for x in range(nl):
        if dp[x - 1] > 0:  # 如果上一个序列的最大子序和大于零就累加，小于零就赋当前值
            dp[x] = dp[x - 1] + num[x]
        else:
            dp[x] = num[x]
        res = max(res, dp[x])  # 每次取最大值
        print(dp)
    return res


print(maxSubArry1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArry1([-2, -1, -3]))

print(maxSubArry2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArry2([-2, -1, -3]))
