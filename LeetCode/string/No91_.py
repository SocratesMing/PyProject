# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).


def numDecodings(s):#动态规划算法
    sl = len(s)
    if sl==0:
        return 0
    dp = [0]*(sl+1)
    dp[0]=1

    if s[0]=="0":
        dp[1]=0
    else:
        dp[1]=1

    for i in range(2,sl+1):

        lastNum = int(s[i-1])
        if lastNum>=1 and lastNum<=9:
            dp[i] +=dp[i-1]
        lastNum = int(s[i-2:i])
        if lastNum >=10 and lastNum<=26:
            dp[i] +=dp[i-2]
    return dp[-1]

print(numDecodings("226"))