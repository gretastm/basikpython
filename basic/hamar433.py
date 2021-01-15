arr=[[13,26,39,41],
     [19,28,36,48],
     [16,25,38,47],
     [11,27,32,43]]
n=len(arr)
a=10
b=40
c=0
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if arr[i][j]>a and arr[i][j]<b:
            c=c+1
print(c)