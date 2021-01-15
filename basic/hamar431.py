a=[[10,83,21,53],
   [4,19,26,31],
   [11,91,78,56],
   [33,42,57,25]]
n=len(a)
b=0
c=0
for i in range(1,n):
    for j in range(n-i,n):
        k=i+j
        if n%2!=0:
            b=b+1
for i in range(n):
    for j in range(n):
        m=i+j
        if m%2!=0:
            c=c+1
d=b+c
print(d)