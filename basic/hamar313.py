import random
def poxel(n=11,a=-6,b=40):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=poxel()
y=[]
for u in range(len(x)):
    if u%2==0:
        x[u]=x[u-1]
        y.append(x[u])
print(y)