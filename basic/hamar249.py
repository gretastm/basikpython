k=int(input("k"))
a=[-3,16,-30,-8,45]
b=0
c=0
for i in range(len(a)):
    import math
    b= math.fabs (a[i]-i)
    if b>k:
        c=c+1
print(c)