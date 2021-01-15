import random
def mecaguyn(n=10,a=10,b=20):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=mecaguyn()
y=[]

for i in x:
    k=i%2==0
    m=k[0]
    for e in k:
        if e>m:
            m=e
            for q in range(len(x)):
                if q%2!=0:
                    q=q+m
                    y.append(q)
print(y)