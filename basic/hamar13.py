a=int(input("a"))
b=int(input("b"))
x=int(input("x"))
import math
e=math.e
c=math.fabs(a+x)
d=math.pow(e,c)
f=math.cos(a+x+b)
g=d*f
h=math.atan(a+x)
j=math.pow(h,1/3)
k=math.fabs(b)+a
if k<5:
    print(g)
elif k>2:
    print(j)
else:
    print(k)