def gumar(x):
    for i in range(1,5):
        k=i
        if x>1:
            import math
            a=k-1
            b=math.pow(x,a)
            print(b)
        elif x<3:
            c=math.pow(k,3)
            d=x*c
            print(d)
        else:
            e=math.pow(10,6)
            f=1/e
            print(f)
gumar(7)