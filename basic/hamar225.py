import random
def bac(n=8,a=-5,b=11):
    c=[]
    for i in range(n):
        d=random.randint(a,b)
        c.append(d)
    return c
o=bac()
t=int(input("t"))
j=1
import math
for i in o:
    h=math.fabs(i)
    if h<t:
        j=j*i
print(j)