import random
def mij(n=7,a=-6,b=12):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=mij()
k=0
j=0
for i in o:
    if i>0:
        k=k+1
    else:
        j=j+1
print(k,j)
