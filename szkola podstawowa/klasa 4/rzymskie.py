def split_str(s):
    return [ch for ch in s]

print("Podaj liczbę od 1 do 3999:")
liczba = input()
b = split_str(liczba)
b = list(b)
l = len(b)
x=""
y=""
z=""
k=""

print("Twoja liczba jako rzymska:")
def rzym():
    j = {"0":"","1":"I", "2":"II" , "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
    d = {"0":"","1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
    s = {"0":"","1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"DM"}
    t = {"1":"M", "2":"MM", "3":"MMM"}
    if (l == 1):
        x = j[b[0]]
        print(x)
    if (l == 2):
        x = d[b[0]]
        y = j[b[1]]
        print(x+y)
    if (l == 3):
        x = s[b[0]]
        y = d[b[1]]
        z = j[b[2]]
        print(x+y+z)
    if (l == 4):
        x = t[b[0]]
        y = s[b[1]]
        z = d[b[2]]
        k = j[b[3]]
        print(x+y+z+k)

        
rzym()














