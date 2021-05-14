# 给定⼀个仅包含数字2-9 的字符串，返回所有它能表示的字⺟组合。给出数字到字⺟的映射如下（与电
# 话按键相同）。注意1 不对应任何字⺟。

letterMap = {
    0: "",
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

res = []


def letterCombinations(s):
    if s == "":
        return res
    findCombination(s, 0, "")
    return res


# dfs必备三个参数 初始参数digits、索引ind、组合s
def findCombination(digits, ind, s):
    print(digits, ind, s)
    if ind == len(digits):  # 如果当前索引满足结果要求，就添加并返回，
        res.append(s)
        return  # return是必须的，否则下一步会越界
    num = digits[ind]
    letter = letterMap[int(num)]#取出要遍历的元素然后遍历（要遍历的条件）
    for x in range(len(letter)):
        findCombination(digits, ind + 1, s + letter[x])#参数更新（索引+1、组合，供下一轮判断）
    # return

print(letterCombinations("23"))
