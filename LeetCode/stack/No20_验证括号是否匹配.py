# Input: "()[]{}"
# Output: true
#
# Input: "(]"
# Output: false
#
# Input: "([)]"
# Output: false

def isValid(s):
    mapdic = {"]": "[", "}": "{", ")": "("}
    stk = []
    for x in s:
        if mapdic.get(x) and mapdic[x] == stk[-1]:
            stk.pop()
        else:
            stk.append(x)
        print(x, stk)

    if len(stk) == 0:
        return True
    else:
        return False


def isValid2(s):
    map = {"]": "[",
           "}": "{",
           ")": "("}
    stack = []
    for x in s:
        if x in ['(', '[', '{']:
            stack.append(x)
        else:
            if map[x] == stack[-1]:
                stack.pop()
        print(stack)

    return len(stack) == 0


print(isValid("()[]{}"))
