import random
def arajin(n=6,a=-20,b=15):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
k=arajin()
x=0
v=0
for i in k:
    if i>0:
        x=x+1
    else:
        v=v+1



def erkrord(n=9,a=-14,b=20):
    o=[]
    for i in range(n):
        d=random.randint(a,b)
        o.append(d)
    return o
m=erkrord()
y=0
u=0
for p in m:
    if p>0:
        y=y+1
    else:
        u=u+1
g=x+y
h=u+v
print(g+h)