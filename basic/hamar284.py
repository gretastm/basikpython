import random
def aicb(n=11,p=9,k=27):
    c=[]
    for u in range(n):
        d=random.randint(p,k)
        c.append(d)
        return c
x=aicb()
a=10
b=20
y=[]
for i in x:
    if i>a and i<b:
        y.append(i)
print(y)