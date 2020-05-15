print("Niech a,b,c będą kolejnymi współczynikami w równaniu:")
print("Wpisz a")
a=input()
a=float(a)
print("Wpisz b")
b=input()
b=float(b)
print("Wpisz c")
c=input()
c=float(c)
if(a==0): #dla a=0 bedzie to funkcja liniowa
    print("Nie jest to równanie kwadratowe! Wprowadź jeszcze raz a:")
    a=input()
    a= float(a)
    x=((b**2)-(4*a*c))
    y=(-b + x**(1/2)) / 2*a
    z=(-b - x**(1/2)) / 2*a
    if(x<0):
        print("Brak miejsc zerowych")
    elif(x==0):
        print("Funkcja ma jedno miejsce zerowe:")
        print(((-b) / (2*a)))
    else:
        print("Są dwa miejsca zerowe:")
        print(y,z)
else:
    x=((b**2)-(4*a*c))
    y=(-b + x**(1/2)) / 2*a
    z=(-b - x**(1/2)) / 2*a
    if(x<0):
        print("Brak miejsc zerowych")
    elif(x==0):
        print("Funkcja ma jedno miejsce zerowe:")
        print(((-b) / (2*a)))
    else:
        print("Są dwa miejsca zerowe:")
        print(y,z)
