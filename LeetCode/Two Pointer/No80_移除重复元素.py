# Given nums = [0,0,1,1,1,1,2,3,3]
# Your function should return length = 7, with the first seven elemen
# being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# It doesn't matter what values are set beyond the returned length.


def removeDuplicate(num):
    last, find, startFind = 0, 0, - 1
    # last：结果数组的最后索引，find当前索引
    nl = len(num) - 1

    while last < nl:
        startFind = -1
        while num[find] == num[last]:
            if startFind == -1 or startFind > find:
                startFind = find
            if find == nl:
                break
            find += 1
        if find - startFind >= 2 and num[find - 1] == num[last] and num[find] != num[
            last]:  # 符合 1 1 2 的情况，此时find在2，last在第一个1
            num[last + 1] = num[find - 1]
            num[last + 2] = num[find]
            last += 2
        else:
            num[last + 1] = num[find]
            last += 1

        if find == nl:  # 边界处理
            if num[find] != num[last - 1]:
                num[last] = num[find]
            print(num)
            return last + 1
        print(num, find, last)


    return last + 1

print(removeDuplicate([0, 0, 1, 1, 1, 1, 2, 3, 3]))
