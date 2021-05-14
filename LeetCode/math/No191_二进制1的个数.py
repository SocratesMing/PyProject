# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary String 11111111111111111111111111111101 has a
# total of thirty one '1' bits.
#


def countWeight1(num):
    count = 0
    while num:
        num = num & (num-1)
        count +=1
        print(bin(num))

    return count

input = 0b00011011011101
print(countWeight1(input))

