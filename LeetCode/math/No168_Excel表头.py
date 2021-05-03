# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB
def excelTitle(num):
    res = ''
    while num:
        res = chr((num-1) % 26 +65)+res
        num = (num-1)//26
        print(num)
    print(res)

# print(ord('B'))
# print(chr(65))
excelTitle(701)
