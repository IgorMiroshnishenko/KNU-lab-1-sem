#Мірошниченко Ігор ІПЗ-13
from math import sin
from math import cos
x=int(input("X="))
p=3.14
if(0<x<p):
    y=sin(x)
    print("first variant")
    print("y=",y)
if(p<x<3*p/2):
    y=cos(x)
    print("second variant")
    print("y=",y)
if(3*p/x<x<2*p):
    y=sin(x)/cos(x)
    print("third variant")
    print("y=",y)
else:
    print("error")
