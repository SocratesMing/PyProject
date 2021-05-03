#

def coinChange(coins, amount):
    dp = [amount + 1 for _ in range(amount+1)]
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                print(dp[1:])
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    if dp[amount] > amount:
        return -1

    return dp[amount]


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11

    re = coinChange(coins, amount)

    print(re)
