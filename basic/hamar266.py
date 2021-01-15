import random
def kent(n=6,a=8,b=16):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
x=kent()
v=0
for i in x:
    if i%2!=0:
        v=v+i

def zuyg(n=5,a=12,b=20):
    o=[]
    for i in range(n):
        d=random.randint(a,b)
        o.append(d)
    return o
y=zuyg()
u=0
for p in y:
    if p%2==0:
        u=u+p
g=v-u
print(g)