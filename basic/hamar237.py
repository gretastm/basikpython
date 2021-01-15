import random
def zro(n=4,a=-2,b=10):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=zro()
l=0
for i in o:
    if i==0:
        l=l+1
print(l)