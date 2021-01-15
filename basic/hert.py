while True:
    a=0
    try:
        b=int(input("mutqagrel tiv"))
    except ValueError:
        continue
    if b==1:
        print("amragrel hert",(a+1))
    elif b==2:
        print("chexarkel herty",(a-1))
    elif b==3:
        print("mardkanc qanaky",a)
    elif b==0:
        break