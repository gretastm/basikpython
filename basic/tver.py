def gumar(n):
    b=0
    while n!=0:
        a=n%10
        n=int(n/10)
        b=b+a
    print(b)

def artadryal(n):
    b=1
    while n!=0:
        a=n%10
        n=int(n/10)
        b=b*a
    print(b)

def agicdzax(n):
    while n!=0:
        a=n%10
        b=int(n/10)
        b=a*10+b
        print(b)
        n=0

def dzaxicaj(n):
    while n!=0:
        a=n%10
        b=int(n/10)
        b=b*10+a
        print(b)
        n=0

def erku(n):
    while n!=0:
        a=n%10
        b=int(n/10)
        if a==2:
            print("true")
        else:
            print("false")
        n=0

def kent(n):
    while n!=0:
        a=n%10
        b=int(n/10)
        if a%2!=0:
            print("true")
        else:
            print("false")
        n=0

def arjeq(n,x):
    import math
    k=1
    while k<=n:
        a=math.pow(x,k)
        print(a)
        k=k+1