# Input: m = 7, n = 3
# Output: 28
# 机器人从左上角到右下角共有多少种走法


def uniquePaht(row, col):
    res = [[0] * col] * row
    res[0][0] = 0  # res存储的是走到当前各自格子共有多少种走法
    for x in range(row):
        for y in range(col):
            if x == 0 and y != 0:  # x
                res[x][y] = 1
            elif x != 0 and y == 0:
                res[x][y] = 1

            else:
                res[x][y] = res[x - 1][y] + res[x][y - 1]

    print(res)
    return res[row - 1][col - 1]


print(uniquePaht(3, 2))

print()
