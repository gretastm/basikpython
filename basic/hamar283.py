import random
def kent(n=8,a=1,b=33):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=kent()
y=[]
for i in x:
    if i%2!=0:
        y.append(i)
print(y)