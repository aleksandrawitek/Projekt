from tkinter import *
from PIL import Image, ImageTk
import os
from subprocess import call
from random import *



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #stworzenie nowego okna
    def init_window(self):

        #nadanie tytułu      
        self.master.title("Platforma Edukacyjna")

def cofnij():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'klasa4.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def odswiez():

    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'rzymskie.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])




def sprawdz():
    userinput= var.get()
    userinput = userinput.upper()
    if (userinput == wynik):
        poprawna = Label(root, text = "Poprawna", background='papaya whip', font = "Arial 30 ", fg = 'Dark Green').place(x= jakax, y=poly)
    else:
        blad = "Poprawny wynik - " + str(wynik)
        niepoprawna = Label(root, text = blad, background='papaya whip', font = "Arial 30 ", fg = 'Red2').place(x= jakax, y=poly)


root = Tk()

#rozmiar okna, dostosowany do wymiarów ekranu uzytkownika

ekran_dl = root.winfo_screenwidth()
ekran_szer = root.winfo_screenheight()
okno_dl = 0.9*ekran_dl
okno_szer = 0.9*ekran_szer
odsx = 1.3*okno_szer
odpy = 0.25*okno_dl
odpx = 0.5*okno_szer
polex = 0.5*okno_szer
poly = 0.15*okno_dl
polx = 0.5*okno_szer
jakax = 0.8*okno_szer
sprx = 0.8*okno_szer


okno_dl = str(int(okno_dl))
okno_szer= str(int(okno_szer))
wymiar = okno_dl + 'x' + okno_szer
root.geometry(wymiar)
app = Window(root)

#dopracowanie detali wyglądu

tekst = Label(root, text = 'Zamień liczbę na rzymską:', font = "Arial 30 ", width = okno_szer, height=4,background='navajo white', fg = 'papaya whip', anchor = CENTER)
tekst.pack()

root.configure(background='papaya whip')


#dodanie przycisków oraz dopracowanie szczegółów ich wyglądu w zaleznosci od wielkosci okna

okno_dl = int(okno_dl)
okno_szer= int(okno_szer)

buttonwidth = int(0.05*okno_dl)
buttonheight = int(0.001*okno_szer)




cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)

liczba = randrange(1,3999,1)
liczba = str(liczba)
def split_str(s):
    return [ch for ch in s]

b = split_str(liczba)
b = list(b)
l = len(b)
x=""
y=""
z=""
k=""



j = {"0":"","1":"I", "2":"II" , "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
d = {"0":"","1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
s = {"0":"","1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"DM"}
t = {"1":"M", "2":"MM", "3":"MMM"}
if (l == 1):
    wynik = j[b[0]]
if (l == 2):
    x = d[b[0]]
    y = j[b[1]]
    wynik = x+y
if (l == 3):
    x = s[b[0]]
    y = d[b[1]]
    z = j[b[2]]
    wynik = x+y+z
if (l == 4):
    x = t[b[0]]
    y = s[b[1]]
    z = d[b[2]]
    k = j[b[3]]
    wynik = x+y+z+k



poleconko = str(liczba)

polecenie = Label(root, text = poleconko, background='papaya whip', font = "Arial 30 ", fg = 'black').place(x= polx, y=poly)
var = StringVar()
odpowiedz = Label(root, text = "Odpowiedz", background='papaya whip', font = "Arial 30 ", fg = 'black').place(x= odpx, y=odpy)
poletekstowe = Entry(root, bd = 10, textvariable=var).place(x= polex, y=odpy)

sprawdzenie = Button(root, text = 'Enter', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = sprawdz).place(x= sprx, y=odpy)



#dodanie zdjęcia u dołu strony dopasowanego do wymiarów okna aplikacji
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'children.png')
children = PhotoImage(file=image_path)
label = Label(image=children, width = okno_dl, height = 0.43 * okno_szer)
label.image = children
label.pack(side = BOTTOM)


root.mainloop()  