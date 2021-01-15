a=[[13,51,63,82],
   [6,8,10,12],
   [86,92,45,75],
   [15,33,21,43]]
n=len(a)
b=0
c=0
d=0
f=0
for i in range(1,n):
    for j in range(0,i):
        if a[i][j]%2==0:
            b=b+a[i][j]
            c=c+1

for i in range(n):
    for a[i][j] in range(n):
        d=d+a[i][j]
        f=f+1
g=b+d
h=c+f
k=g/h
print(k)