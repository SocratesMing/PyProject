s = "{[]}"

def match(s):
    map = {"]":"[",
           "}":"{",
           ")":"("}
    stack = []
    for x in s:
        if x in ['(','[','{']:
            stack.append(x)
        else:
            if map[x]==stack[-1]:
                stack.pop()
        print(stack)

    return len(stack)==0

print(match(s))
