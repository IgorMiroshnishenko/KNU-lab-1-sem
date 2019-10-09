from math import inf
from math import factorial
r,x=0.0,1
while(x<5):
    k=0
    while(k<170):
        r+=((-1)**k*(k+1)*x**k)/factorial(k)
        k+=1
        print(r)
    x+=1
    print(r)