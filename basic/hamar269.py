x=[1,2,3,4]
y=[5,6,7,8]
a=0
b=0
for i in range(len(x)):
    if i%2==0:
        a=a+x[i]
for k in range(len(y)):
    if k%2!=0:
        b=b+y[k]
print(a+b)