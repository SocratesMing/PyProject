
res = {}
def convert(js,s):
    for k,v in js.items():
        s= k+"."+s
        if type(v)==dict:
            convert(v,s)
        else:
            res[s]=v

def converNew(js):
    convert(js,"")

dic = {"a": {"b": {"c": {"dd": 'abcdd'}},"d": {"xx": 'adxx'},"e": 'ae'}}

converNew(dic)
print(res)