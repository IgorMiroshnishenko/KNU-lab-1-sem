                                #Лабораторна робота №1
Автор: ірошниченко Ігор

Група: ІПЗ-13

Варіант: 15
---
Завдання складаеться з двох частин.
---
(1Частина)

Ім'я, Прізвище, ПІБ Вашого класного керівника
- Прізвище, ім'я ( "Ваші прізвище, ім'я?")
- ПІБ Вашого класного керівника ( "ПІБ Вашого класного керівника?")

Після цього виводила б три рядки:
"Ваші ім'я, прізвище"
"ПІБ Вашого керівника з інформатики"
----
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

(2Частин)

X=((1 - A)CeA)/((1-B)CosD)
--------------------
#2

A=int(input("A="))

B=int(input("B="))

C=int(input("C="))

D=int(input("D="))

X=(A**2/fabs(1-B))+(B**2/fabs(1-D))+(C**2/log10(A))

print(X)