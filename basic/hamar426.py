a=[[1,13,26,84,],
   [12,26,47,64],
   [14,78,31,47],
   [8,15,63,44]]
n=len(a)
s=0
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[i][j]%2==0:
            s=s+a[i][j]
print(s)