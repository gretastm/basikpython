def ex281(arr):
    a=list(filter(lambda x:x>0,arr))
    a2=list(map(lambda x:x>0,arr))
    print(a,a2)

def ex282(arr):
    b=list(filter(lambda x:x!=0,arr))
    b2=list(map(lambda x:x!=0,arr))
    print(b,b2)


def ex283(arr):
    c=list(filter(lambda x:x%2!=0,arr))
    c2=list(map(lambda x:x%2!=0,arr))
    print(c,c2)

def ex284(arr,a,b):
    d=list(filter(lambda x:a<x and x<b,arr))
    d2=list(map(lambda x:a<x and x<b,arr))
    print(d,d2)


def ex285(arr,p):
    e=list((filter(lambda x:x%p==0,arr)))
    e2=list(map(lambda x:x%p==0,arr))
    print(e,e2)
def ex286(arr):
    f=list(filter(lambda x:x%2==0,arr))
    f2=list(map(lambda x:x%2==0,arr))
    print(f,f2)


def ex290(arr):
    g=list(filter(lambda x:x%6==1,arr))
    g2=list(map(lambda x:x%6==1,arr))
    print(g,g2)