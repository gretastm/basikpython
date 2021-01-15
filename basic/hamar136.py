def havasar(x):
    for i in range(2,9):
        k=i
        if x>3 and x<7:
            import math
            a=math.pow(x,k)
            b=9*a
            print(b)
        else:
            c=8*x
            d=math.pow(k,3)
            e=c+d
            print(e)
havasar(5)