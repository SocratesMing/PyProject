# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def longestNorepeatString(s):
    left, right, res = 0, 1, 1
    if len(s) == 1:
        return 1
    else:

        while right < len(s):
            # print(s[left:right], left, right, s[right], res)
            if s[right] not in s[left:right]:
                right += 1
            else:
                left += 1
            res = max(res, right - left)
            # print("dddd")
        return res


input = "pwwkew"
output = longestNorepeatString(input)
print(output)
