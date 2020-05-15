from random import *
def dzielenie():
    a = randrange(1,1000,1)
    b = randrange(1,1000,1)
    while (a%b != 0):
        b = randrange(1,1000,1)
    iloraz = a / b
    iloraz = int(iloraz)
    