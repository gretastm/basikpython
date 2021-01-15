class Vecror:
    def __init__(self,arr):
        m=arr[0]
        for i in arr:
            if i > m:
                m = i
        for v in arr:
            if v > 0:
                v +=m
    def zero(self,arr):
        for i in range(len(arr)):
            if arr[i]>0:
                arr[i+1]=0
    def poqr(self,arr):
        arr2=[]
        import math
        m=arr[0]
        k=0
        p=0
        for i in arr:
            if i>m:
                m=i
            else:
                k+=i
                p+=(k+m)/2
                b=math.fabs(i)
                if b<p:
                    arr2.append(i)
    def heracel(self,arr):
        m=arr[0]
        a=0
        for i in range(len(arr)):
            if arr[i]>m:
                m=arr[i]
            else:
                a+=arr[i]
            if arr[i]==a:
                del arr[i]
            elif arr[i]==m:
                del arr[i]
    def zero2(self,arr):
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i+1]=0
                arr[i+2]=0
    def mec(self,arr):
        arr2 = []
        m = arr[0]
        k = 0
        p = 0
        for i in arr:
            if i > m:
                m = i
            else:
                k += i
                p += (k + m)/2
                if i>p:
                    arr2.append(i)
    def veragrel(self,arr):
        a=arr[0]
        m=0
        for i in arr:
            if i>a:
                m+=i
                a=a+m
                m=a-m
                a=a-m
    def arajinverjin(self,arr):
        for i in range(len(arr)):
            a=arr[0]
            b=arr[-1]
            c=0
            c=a
            a=b
            b=c
    def tarrindex(self,arr):
        arr2=[]
        p=arr[0]
        for i in range(len(arr)):
            if i<p:
                p=i
                if arr[i]==p:
                    arr2.append(arr[i])
    def zuyg(self,arr):
        arr2=[]
        for i in arr:
            if i%2==0:
                arr2.append(i)
                for x in arr:
                    if x%2!=0:
                        arr2.append(x)
    def mecpoqr(self,arr):
        a=arr[0]
        b=0
        for i in arr:
            if i>a:
                a=i
            else:
                b+=i
                c=b**2
                d=a**3
                for x in arr:
                    if x==a:
                        a=c
                    elif x==b:
                        b=d