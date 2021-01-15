import random
def qanak(n=5,a=-10,b=8):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=qanak()
k=0
j=0
for i in o:
    if i <0:
     import math
     i=math.pow(i,2)
     k=k+i
     j=math.sqrt(k)
print(j)

