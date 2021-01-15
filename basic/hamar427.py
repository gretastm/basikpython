a=[[10,20,30,40],
   [50,60,70,80],
   [48,56,62,36],
   [90,51,17,52,]]
n=len(a)
k=int(input("k"))
b=1
c=1
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[i][j]%k==0:
            b=b*a[i][j]
for i in range(n):
    for j in range(n):
        if a[i][j]%k==0:
            c=c*a[i][j]
d=b*c
print(d)