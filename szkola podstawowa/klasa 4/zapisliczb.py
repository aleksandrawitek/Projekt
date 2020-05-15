def split_str(s):
    return [ch for ch in s]

print("Podaj liczbę od 1 do 1999:")
liczba = input()
b = split_str(liczba)
b = list(b)
l = len(b)
x=""
y=""
z=""
k=""

print("Twoja liczba slownie:")
def slow():
    j = {"0":"","1":"jeden", "2":"dwa" , "3":"trzy", "4":"cztery", "5":"pięć", "6":"sześć", "7":"siedem", "8":"osiem", "9":"dziewięć", "10":"dziesięć", "11":"jedenaście", "12":"dwanaście", "13":"trzynaście", "14":"czternaście", "15":"piętnaście", "16":"szesnaście", "17":"siedemnaście", "18":"osiemnaście", "19":"dziewiętnaście"}
    d = {"0":"", "2":"dwadzieścia", "3":"trzydzieści", "4":"czterdzieści", "5":"pięćdziesiąt", "6":"sześćdziesiąt", "7":"siedemdziesiąt", "8":"osiemdziesiąt", "9":"dziewięćdziesiąt"}
    s = {"0":"","1":"sto", "2":"dwieście", "3":"trzysta", "4":"czterysta", "5":"pięćset", "6":"sześćset", "7":"siedemset", "8":"osiemset", "9":"dziewięćset"}
    t = {"1":"tysiąc"}
    if (l == 1):
        x = j[b[0]]
        print(x)
    if (l == 2):
        if (b[0] == "1"):
            liczba = b[0]+b[1]
            nascie = j[liczba]
            print(nascie)
        else:
            x = d[b[0]]
            y = j[b[1]]
            print(x+" "+y)
            
    if (l == 3):
        if (b[1] == "1"):
            x = s[b[0]] + " "
            liczba = b[1]+b[2]
            nascie = j[liczba]
            print(x+nascie)
        else:
            x = s[b[0]] + " "
            y = d[b[1]] + " "
            z = j[b[2]]
            print(x+y+z)
    if (l == 4):
        if (b[2] == "1"):
            x = t[b[0]] + " "
            y = s[b[1]] + " "
            liczba = b[2]+b[3]
            nascie = j[liczba]
            print(x+y+nascie)
        else:
            x = t[b[0]] + " "
            y = s[b[1]] + " "
            z = d[b[2]] + " "
            k = j[b[3]]
            print(x+y+z+k)

        
slow()














