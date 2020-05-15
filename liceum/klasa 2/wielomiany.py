def wielomian(x, *args): #kolejne wartosci wspolczynnikow wielomianu 
        suma = 0
        for i in args:
            suma += i * (x**i)
        return suma
