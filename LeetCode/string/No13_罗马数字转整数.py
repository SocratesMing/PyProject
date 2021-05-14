# 字符  数值
# I  1
# V  5
# X  10
# L  50
# C  100
# D  500
# M  1000
# I 可以放在V (5) 和X (10) 的左边，来表示4 和9。
# X 可以放在L (50) 和C (100) 的左边，来表示40 和90。
# C 可以放在D (500) 和M (1000) 的左边，来表示400 和900。


def Roma2Int(s):
    roman = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000, }

    res, l, lastInt = 0, len(s), 0  # lastInt当前元素的前一个元素到最右边的和

    for x in range(l):
        v = roman[s[-1 - x]]
        if v < lastInt:  #比较当前元素和lastInt
            res -= v
        else:
            res += v
        lastInt = res
    return res


print(Roma2Int("MCMXCIV"))
print(Roma2Int("IX"))
