import random
def mnac(n=8,a=-5,b=10):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=mnac()
g=1
for i in range(len(o)):
    k=o[i]*i
    if k%3==2:
        e=k**2
        g=g*e
print(g)