import random
def zuyg(n=8,a=11,b=30):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=zuyg()
y=[]
for i in x:
    if i%2==0:
        y.append(i)
print(y)