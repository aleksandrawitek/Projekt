def obwod(a,b,c):
    print("Twój obwód to:")
    print(a+b+c)
def pole(a,b,c):
    #skorzystamy ze wzoru na pole 
    #(p(p-a)(p-b)(p-c))^1/2, gdzie p to polowa obwodu
    p = ((a+b+c) / 2)
    po = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print("Twoje pole to:")
    print(po)
def jaki(a,b,c):
    if(a == b and b != c):
        print("Trójkąt jest równoramienny")
    elif(a == c and a != b):
        print("Trójkąt jest równoramienny")
    elif(b == c and b != a):
        print("Trójkąt jest równoramienny")
    elif(a == c and a == b and b == c):
        print("Trójkąt jest równoboczny")
    else:
        print("Trójkąt jest róznoboczny")
def rodzaj(a,b,c):
    if(a**2 + b**2 == c**2):
        print("Trójkąt jest prostokątny")
    elif(a**2 + b**2 < c**2):
        print("Trójkąt jest rozwartokątny")
    else:
        print("Trójkąt jest ostrokątny")


