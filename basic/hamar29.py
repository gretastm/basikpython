def akarg(a,b,c):
    if a<b and b<c:
        print(a,b,c)
    elif a<b and b>c:
        if a<c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif a>b and b<c:
        if a<c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)
akarg(6,4,2)

