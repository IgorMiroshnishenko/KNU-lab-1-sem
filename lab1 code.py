#Мірошниченко Ігор ІПЗ-13
#1
import math
from math import fabs
from math import log10
print("Мірошниченко Ігор")
print("Шрупа ІПЗ-13")
print("Enter your name")
N=input()
print("Enter your sername")
S=input()
print("Enter your contry")
K=input()
print("Enter your City")
T=input()
print(N)
print(S)
print(K)
print(T)

#2

A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
D=int(input("D="))
X=(A**2/fabs(1-B))+(B**2/fabs(1-D))+(C**2/log10(A))
print(X)
