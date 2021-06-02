from copy import deepcopy

a = [1,2,3,4,["a","b"]]
b = "xxx"
c = "xxx"
d = "xxx"
#对a进行操作
a[-1].append("c")
a.append(5)
b = a.copy()
c= deepcopy(a)
c.pop()
d=deepcopy(c)
d[-1].pop()
# 使得输出结果如下：
print(a)  #[1,2,3,4,[a,b,c,],5]
print(b)  #[1,2,3,4,[a,b,c,],5]
print(c)  #[1,2,3,4,[a,b,c,]]
print(d)  #[1,2,3,4,[a,b]]