import random
def kentindeqs(n=5,a=25,b=35):
    c=[]
    for u in range(n):
        d=random.randint(a,b)
        c.append(d)
        return c
x=kentindeqs()
y=[]
for i in range(len(x)):
    if i%2!=0:
        y.append(x[i])
print(y)