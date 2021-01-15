import random
def tarreri(n=4,a=5,b=17):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=tarreri()
n=0
for i in x:
    h=i**2
    n=n+h

def qarakusi(n=3,a=-7,b=16):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
y=qarakusi()
m=0
for t in y:
    g=t**2
    m=m+t
q=n+m
print(q)