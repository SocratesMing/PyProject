# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying
# price.

def bestProfit(num):  # 暴力解法，依次遍历取差值最大的即可
    res = 0
    nl = len(num)

    for x in range(nl):
        for y in range(x + 1, nl):
            p = num[y] - num[x]
            print(p)
            if p > res:
                res = p
    return res


def bestProfit2(num):  # 动态规划，感觉也不算是动态规划
    nl = len(num)
    min, maxpf = num[0], 0  # 记录最小值，然后做差
    for i in range(1, nl):
        if num[i] - min > maxpf:  # 当前值与最小值做差大于最大收益，替换
            maxpf = num[i] - min
        if num[i] < min:  # 当前值比最小值小，替换最小值
            min = num[i]
    return maxpf


def bestProfit3(num):  # 单调栈
    nl = len(num)
    if nl == 0:
        return 0
    stk, res = [num[0]], 0

    for i in range(1, nl):
        if num[i] > stk[-1]:  # 当前元素比栈中元素大就添加到栈顶
            stk.append(num[i])
        else:
            ind = len(stk) - 1
            while ind >= 0:
                if stk[ind] < num[i]:
                    break
                ind -= 1
            stk = stk[:ind + 1]
            stk.append(num[i])
        res = max(res, stk[-1] - stk[0])
    return res


# print(bestProfit( [7,1,5,3,6,4]))
# print(bestProfit2([7, 1, 5, 3, 6, 4]))
print(bestProfit3([7, 1, 5, 3, 6, 4]))
