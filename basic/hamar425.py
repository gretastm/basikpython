a=[[11,22,33,44],
   [55,66,77,88,],
   [12,23,34,45],
   [7,8,9,10]]
n=len(a)
b=0
for i in range(1,n):
    for j in range(0,i):
        if a[i][j]%2==0:
            b=b+1
print(b)