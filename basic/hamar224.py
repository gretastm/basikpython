k=int(input("k"))
a=[-5,3,11,-23,65,-89]
b=0
for i in a:
    import math
    c=math.fabs(i)
    if c<k:
        d=math.pow(i,3)
        b=b+d
print(b)