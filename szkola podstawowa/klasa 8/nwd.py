def nwd(a,b):
    nwd = 1
    if a%b == 0:
        return b
        print(b)
    for x in range(int(b/2), 0, -1):
        if a%x == 0 and b%x == 0:
            nwd = x
            print(x)
            break
    return nwd
    
print("Wpisz calkowitą liczbę a:")
a = input()
a = int(a)
print("Wpisz calkowita liczbę b:")
b = input()
b = int(b)
print("Najwiekszy wspolny dzielnik to:")
nwd(a,b)


    

