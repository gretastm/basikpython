import random
def matrix(a,b):
    arr=[]
    for i in range(a):
        arr.append([])
        for j in range(b):
            arr[-1].append(random.randint(-100,100))
        return arr
class Solution():
    def mijin(self):
        matrix(4,4)
    a=0
    import math
    n=len(matrix(4,4))
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if (i+j)%2!=0:
                b=math.pow(matrix(4,4)[i][j],2)
                a+=b
                c=math.sqrt(a)
                print(c)
    def qanak(self):
        matrix(4,4)
        a=0
        n=len(matrix(4,4))
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if (matrix(4,4)[i][j])%5==0:
                    a+=1
                    return a
    def mijtv(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=5
        b=10
        c=0
        d=0
        for i in range(1,n):
            for j in range(0,i):
                if matrix(4,4)[i][j]>a and matrix(4,4)<b:
                    c+=matrix(4,4)[i][j]
                    d+=1
                    print(c/d)
    def artadryal(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=1
        for i in range(0,n-1):
            for j in range(i+1,n):
                if (i+j)!=0:
                    a*=matrix(4,4)[i][j]
                    print(a)
    def gumar(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=0
        for i in range(0,n-1):
            for j in range(i+1,n):
                if (i+j)%2==0:
                    a+=matrix(4,4)[i][j]
                    print(a)
    def mijtv2(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=0
        b=0
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if matrix(4,4)[i][j]<0:
                    a+=matrix(4,4)[i][j]
                    b+=1
                    print(a/b)
    def meck(self):
        matrix(4,4)
        n=len(matrix(4,4))
        k=10
        a=0
        for i in range(1,n):
            for j in range(0,i):
                import math
                if math.fabs(matrix(4,4)[i][j])>k:
                    a+=1
                    print(a)
    def poqrk(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=10
        b=1
        for i in range(1,n):
            for j in range(n-i,n):
                if matrix(4,4)[i][j]<a:
                    b*=matrix(4,4)[i][j]
                    print(b)
    def bazm4(self):
        matrix(4,4)
        n=len(matrix(4,4))
        a=0
        for i in range(1,n):
            for j in range(n-i,n):
                if matrix(4,4)[i][j]%4==0:
                    a+=matrix(4,4)[i][j]
                    print(a)