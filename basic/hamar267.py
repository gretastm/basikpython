import random
def bazma(n=11,a=1,b=15):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=bazma()
v=0
for i in x:
    if i%7==0:
        v=v+i

def patik(n=10,a=6,b=18):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
y=patik()
u=0
for k in y:
    if k%7==0:
        u=u+k
j=v+u
print(j)