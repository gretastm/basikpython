import math
a=[13,-7,2,-5,10]
b=0
c=0
d=0
for i in a:
    if i <0:
        c=math.pow(i,2)
        d=d+c
        b=math.sqrt(d)
print(b)