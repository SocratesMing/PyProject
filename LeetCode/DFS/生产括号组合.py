


def generateParenthesis(n):
    res = []
    s = ""
    findGenerateParenthesis(n,n,s,res)
    return res

def findGenerateParenthesis(lind,rind,s,res):
    print(s)
    if lind==0 and rind==0:
        print("****")
        res.apped(s)

    if lind>0:
        findGenerateParenthesis(lind-1,rind,s+"(",res)

    if lind>0 and lind<rind:
        findGenerateParenthesis(lind, rind-1, s + ")",res)


print(generateParenthesis(3))