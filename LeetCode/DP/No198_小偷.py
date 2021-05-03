# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12
#
# House Robber
# 不停地累加考虑用动态规划算法
def houseRobber(arr):

    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        dp=[0]*len(arr)
        dp[0],dp[1]=arr[0],arr[1]
        for i in range(2,len(arr)):
            dp[i] = arr[i]+dp[i-2]
            print(dp[i])

        return max(dp[i],dp[i-1])

input = [2,7,9,3,1]
print(houseRobber(input))