a=[[15,17,16,29],
   [78,22,91,34],
   [51,18,76,61],
   [11,85,68,36]]
n=len(a)
b=0
c=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i][j]%5==2:
            b=b+1
for i in range(n):
    for j in range(n):
        if a[i][j]%5==2:
            c=c+1
d=c+b
print(d)