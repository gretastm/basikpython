import random
def mecaguyn(n=7,a=-11,b=33):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=mecaguyn()
m=x[0]
y=[]
for i in x:
    if i>m:
        m=i
        for v in x:
            if v>0:
                v=v+m
                y.append(v)
print(y)