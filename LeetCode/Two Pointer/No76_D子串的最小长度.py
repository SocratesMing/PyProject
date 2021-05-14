#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

def minWindow(s,t):
    result, left, right, finalLeft, finalRight, minW, count = "", 0, -1, -1, -1, len(s) + 1, 0