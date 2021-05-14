# 给定两个整数，被除数dividend 和除数divisor。将两数相除，要求不使⽤乘法、除法和mod 运算
# 符。返回被除数dividend 除以除数divisor 得到的商。
#
# Input: dividend = 10, divisor = 3
# Output: 3

def divided(dvd, dvs):
    if dvd == 0:
        return 0
    if dvs == 1:
        return dvd

    sign = -1
    if dvd > 0 and dvs > 0 or dvd < 0 and dvs < 0:
        sign = 1

    dvd, dvs = abs(dvd), abs(dvs)
    res = 0

    while dvd > dvs:
        temp = dvs
        m = 1
        while temp << 1 < dvd:
            temp <<= 1  # 除数不停地乘2
            m <<= 1  # 倍数不停地乘2
            # print(temp, dvd, m)

        res += m
        dvd -= temp  # 差值返回下一轮继续除以除数
        # print(temp, dvd, m)

    return sign * res


print(divided(100, 6))
# print(divided(-10,3))
