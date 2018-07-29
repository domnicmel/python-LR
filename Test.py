#7
from time import time
from math import sqrt
start = time()

l =[2]
a =3
sw =True
while sw:
    for i in l:
        if len(l)==10001:
            sw =False
        elif i<=int(sqrt(a)+1) and a%i==0:
            a=a+2
        elif all(a%i!=0 for i in l) :
            l.append(a)
            a=a+2

print(l[-1])
print(time()-start)