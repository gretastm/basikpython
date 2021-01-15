def ex434(arr):
    s=0
    a=5.4
    b=15.3
    n=len(arr)
    for i in range(1,n):
        for j in range(n-i,n):
            import math
            c=math.fabs(arr[i][j])
            if c>a and c<b:
                s=s+arr[i][j]
                print(s)
arr=[[1,2,5],
     [3,4,6],
     [4,8,9]]
ex434(arr)


def ex436(arr):
    a=10
    b=20
    c=0
    d=0
    n=len(arr)
    for i in range(1,n):
        for j in range(0,i):
            if arr[i][j]>a and arr[i][j]<b:
                c=c+arr[i][j]
                d=d+1
                print(c/d)
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
ex436(arr)



def ex437(arr):
    a=0
    b=0
    n=len(arr)
    for i in range(1,n):
        for j in range(0,i):
            import math
            b=b+math.pow(arr[i][j],2)
            a=a+math.sqrt(b)
            print(a)

arr=[[1,5,3],
     [2,4,8],
     [6,7,9]]
ex437(arr)

def ex438(arr):
    n=len(arr)
    c=0
    for i in range(1,n):
        for j in range(0,i):
            if j%2==0 and arr[i][j]>0:
                c=c+1
                print(c)
arr=[[11,22,33],
     [44,55,66],
     [77,88,99]]
ex438(arr)

def ex439(arr):
    n=len(arr)
    a=1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (i+j)%2!=0:
                a=a*arr[i][j]
                print(a)
arr=[[23,50,13],
     [15,32,41],
     [6,5,12]]
ex439(arr)



def ex440(arr):
    n=len(arr)
    s=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (i+j)%2==0:
                s=s+arr[i][j]
                print(s)
arr=[[1,15,17],
     [9,51,64],
     [5,41,36]]
ex440(arr)

def ex441(arr):
    n=len(arr)
    a=0
    b=0
    for i in range(0,n-1):
        for j in range(i+1):
            import math
            if arr[i][j] > 0:
                b=b+math.pow(arr[i][j],2)
                a=a+math.sqrt(b)
                print(a)
arr=[[-5,23,11],
     [7,-11,53],
     [10,37,-5]]
ex441(arr)

def ex442(arr):
    n=len(arr)
    a=0
    b=0
    for i in range(0,n-1):
        for j in range(n-1-i):
            if arr[i][j]<0:
                a=a+arr[i][j]
                b=b+1
                print(a/b)
arr=[[1,-5,10,-9],
     [6,-30,41,-7],
     [8,-23,20,-33],
     [15,-25,13,-53]]
ex442(arr)

def ex445(arr):
    n=len(arr)
    c=0
    k=20
    for i in range(1,n):
        for j in range(0,i):
            import math
            a=math.fabs(arr[i][j])
            if a>k:
                c=c+1
                print(c)
arr=[[-12,21,34],
     [10,-26,31],
     [19,25,-36]]
ex445(arr)

def ex447(arr):
    n=len(arr)
    a=20
    b=1
    for i in range(1,n):
        for j in range(n-i,n):
            if arr[i][j]<a:
                b=b*arr[i][j]
                print(b)
arr=[[5,10,15],
     [9,11,25],
     [18,25,6]]
ex447(arr)

def ex449(arr):
    n=len(arr)
    s=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[i][j]%4==0:
                s=s+arr[i][j]
                print(s)
arr=[[16,4,12],
     [7,8,20],
     [9,24,10]]
ex449(arr)