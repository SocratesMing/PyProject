# Input: "()[]{}"
# Output: true
#
# Input: "(]"
# Output: false
#
# Input: "([)]"
# Output: false

def isValid(s):
    mapdic = {"]":"[","}":"{",")":"("}
    stk = []
    for x in s:
        if mapdic.get(x) and mapdic[x] == stk[-1]:
            stk.pop()
        else:
            stk.append(x)
        print(x,stk)

    if len(stk)==0:
        return True
    else:
        return False

print(isValid("()[]{}"))


