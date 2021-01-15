a=[[1,5,7,6,],
   [2,10,15,4],
   [9,13,1,8],
   [15,21,3,7]]
n=len(a)
k=int(input("k"))
b=0
for i in range(1,n):
    for j in range(0,i):
        if a[i][j]%k==0:
            b=b+1
print(b)