class zangvac:
    def __init__(self,arr):
        a=0
        b=0
        for i in arr:
            if i>0:
                a+=i
                b+=1
                c=a/b
                print(c)
    def migin(self,arr):
        d=0
        e=0
        for i in arr:
            if i<0:
                d+=i
                e+=1
                f=d/e
                print(f)
    def zuyg(self,arr):
        g=1
        n=len(arr)
        for i in range(0,n):
            if i%2==0:
                g*=arr[i]
                print(g)
    def bacardzak(self,arr):
        import math
        h=0
        n=len(arr)
        for i in range(0,n):
            if i%2!=0:
                j=math.fabs(arr[i])
                h+=j
                print(h)
    def qanak(self,arr):
        k=0
        l=0
        for i in arr:
            if i>0:
                k+=1
            else:
                l+=1
                print(k,l)
    def abpatkanel(self,arr):
        a=10
        b=20
        c=0
        for i in arr:
            if i>a and i<b:
                c+=1
                print(c)
    def poqr(self,arr):
        import math
        t=10
        u=1
        for i in arr:
            y=math.fabs(i)
            if y<t:
                u*=i
                print(u)
    def bazmapatik(self,arr):
        k=2
        m=0
        p=0
        n=len(arr)
        for i in range(0,n):
            if i%k==0:
                m+=arr[i]
                p+=1
                s=m/p
                print(s)
    def drakan(self,arr):
        r=1
        n=len(arr)
        for i in range(0,n):
            if arr[i]-i>0:
                r*=arr[i]
                print(r)
    def mijinqarakusayin(self,arr):
        k=10
        a=0
        import math
        for i in arr:
            if i%k==0:
                z=math.pow(i,2)
                a+=z
                b=math.sqrt(a)
                print(b)