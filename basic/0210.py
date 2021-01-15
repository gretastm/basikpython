def ex1(n):
    if n==1:
        return 1
    return n+ex1(n-1)

def ex2(a):
    if len(a)==0:
        return
    print(a[0])
    ex2(a[1:])

def ex4():
    f=open("file.txt")
    a=f.readlines()
    b=a[0]
    c=0
    d=b[1]
    g=0
    j=a[2]
    for i in b:
        if i=="a":
            c=c+1
    for x in d:
        if x=="z":
            g=g+1
            o=len(j)
            print(c,g,o)
    f.close()


def ex5():
    f=open("file.txt")
    c=f.readlines()
    s=0
    for i in c:
        s+=int(i)
    print(s)
    f.close()

def ex6():
    o=0
    f=open("file.txt")
    c=f.readlines()

    d=c[0]
    q=c[1]
    h=c[2]
    i=10
    if len(d)<i:
        o+=1
    elif len(q)<i:
        o+=1
    elif len(h)>i:
        o+=1
        print(o)
        f.close()
def ex7():
    a=0
    f=open("file.txt","r")
    c=f.readline().split(",")
    for i in range(len(c)):
        if i%2!=0:
            a=a+int(c[i])
    print(a/len(c))
    f.close()

def artadryal(n):
    b=1
    while n!=0:
        a=n%10
        b=int(n/10)
        b=b*a
    print(b)

def parz(n):
    a=0
    for i in range(1,n+1):
        if n%i==0:
            a=a+1
            if a==2:
                print("true")
            else:
                print("false")