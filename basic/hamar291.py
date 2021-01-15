import random
def drakan(n=10,a=-20,b=20):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=drakan()
y=[]
for i in x:
    if i>0:
        y.append(i)
print(y)