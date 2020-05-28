from random import *

a = randrange(1,1000,1)
b = randrange(1,1000,1)
while (a < b):
    b = randrange(1,1000,1)
iloraz = a / b
iloraz = int(iloraz)
reszta = a % b
print(a)
print(b)
print(iloraz)
print(reszta)
