a=[[0,1,2,3],
   [11,34,0,7],
   [17,0,35,81],
   [51,62,16,0]]
n=len(a)
b=0
c=0
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[i][j]==0:
            b=b+1
for i in range(n):
    for j in range(n):
        if a[i][j]==0:
            c=c+1
d=b+c
print(d)