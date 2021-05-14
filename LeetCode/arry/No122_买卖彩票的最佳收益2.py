# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them
# later, as you are
# engaging multiple transactions at the same time. You must sell
# before buying again.

def bestProfit(num):  # 前一个比后一个大就累加
    prf = 0
    for x in range(len(num) - 1):
        if num[x + 1] > num[x]:
            prf += num[x + 1] - num[x]
    return prf


print(bestProfit([7, 1, 5, 3, 6, 4]))
