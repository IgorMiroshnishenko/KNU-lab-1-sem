                                      #Лабораторна робота №2
Автор: ірошниченко Ігор

Група: ІПЗ-13

Варіант: 15

----
 [Завдання](https://photos.app.goo.gl/4GCkQX21V3E9g4YU9)
----------------
 
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
