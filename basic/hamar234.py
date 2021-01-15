import random
def kent(n=7,a=-2,b=13):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=kent()
k=0
l=0
for i in o:
    if i!=0:
        k=k+i
        l=l+1
j=k/l
print(j)