import random
def mekmn(n=10,a=28,b=82):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=mekmn()
y=[]
for i in x:
    if i%6==1:
        y.append(i)
print(y)