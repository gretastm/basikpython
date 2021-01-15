import random
def zuyg(n=10,a=8,b=20):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=zuyg()
y=[]
k=int(input("k"))
for i in x:
    p=i**2
    if p<k:
        y.append(i)
print(y)