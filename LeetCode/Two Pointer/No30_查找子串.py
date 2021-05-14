# 给定⼀个源字符串s，再给⼀个字符串数组，要求在源字符串中找到由字符串数组各种组合组成的连续
# 串的起始下标，如果存在多个，在结果中都需要输出。


# 思路
# 这⼀题看似很难，但是有2 个限定条件也导致这题不是特别难。1. 字符串数组⾥⾯的字符串⻓度都是⼀
# 样的。2. 要求字符串数组中的字符串都要连续连在⼀起的，前后顺序可以是任意排列组合。
# 解题思路，先将字符串数组⾥⾯的所有字符串都存到map 中，并累计出现的次数。然后从源字符串从
# 头开始扫，每次判断字符串数组⾥⾯的字符串时候全部都⽤完了(计数是否为0)，如果全部都⽤完了，
# 并且⻓度正好是字符串数组任意排列组合的总⻓度，就记录下这个组合的起始下标。如果不符合，就继
# 续考察源字符串的下⼀个字符，直到扫完整个源字符串。
from copy import deepcopy

def findSubString(s, sub):
    subMap = {}
    for x in sub:
        if subMap.get(x) == None:
            subMap[x] = 1
        else:
            subMap[x] += 1

    subl = len(sub[0])

    res, index = [], 0
    while index < len(s):
        subMap2 = deepcopy(subMap)
        for x in range(len(sub)):
            ssub = s[x * subl + index:(x + 1) * subl + index]
            # print(ssub)
            if subMap2.get(ssub):#如果能找到且不为零，则减一
                subMap2[ssub] -= 1
            else:
                break

        # print(subMap2)
        n = 0
        for k, v in subMap2.items():#开始校验map是否全部减为0
            if v != 0:
                break
            else:
                n += 1
        if n == len(sub):
            res.append(index)
        index += subl

    return res


print(findSubString("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(findSubString("barfoothefoobarman", ["foo", "bar"]))
