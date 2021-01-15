a=[[16,20,7,4,],
   [36,2,11,80],
   [23,9,10,14],
   [8,31,15,44]]
import math
n=len(a)
s=0
k=0
for i in range(1,n):
    for j in range(0,i):
        if a[i][j]%2==0:
            b=math.pow(a[i][j],2)
            s=s+b
for i in range(n):
    for j in range(n):
        if a[i][j]%2==0:
            c=math.pow(j,2)
            k=k+c
d=s+k
f=math.sqrt(d)
print(f)