k=int(input("k"))
a=[1,-5,13,-10,20]
b=0
for i in range(len(a)):
    if i%k==0:
        b=b+a[i]
print(b)