from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
from subprocess import call


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #stworzenie nowego okna
    def init_window(self):

        #nadanie tytułu      
        self.master.title("Platforma Edukacyjna")

def openpodst():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'podstawowka.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])


def openlo():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'liceum.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])
    
root = Tk()

#rozmiar okna, dostosowany do wymiarów ekranu uzytkownika

ekran_dl = root.winfo_screenwidth()
ekran_szer = root.winfo_screenheight()
okno_dl = 0.9*ekran_dl
okno_szer = 0.9*ekran_szer
okno_dl = str(int(okno_dl))
okno_szer= str(int(okno_szer))
wymiar = okno_dl + 'x' + okno_szer
root.geometry(wymiar)
app = Window(root)

#dopracowanie detali wyglądu

tekst = Label(root, text = 'Wybierz etap edukacji:', font = "Arial 30 ", width = okno_szer, height=4,background='CadetBlue3', fg = 'PaleTurquoise1', anchor = CENTER)
tekst.pack()

root.configure(background='PaleTurquoise1')

#dodanie przycisków oraz dopracowanie szczegółów ich wyglądu w zaleznosci od wielkosci okna

okno_dl = int(okno_dl)
okno_szer= int(okno_szer)

buttonwidth = int(0.05*okno_dl)
buttonheight = int(0.005*okno_szer)
button1x = 0.35*okno_szer
button1y = 0.15*okno_dl
button2x = 0.35*okno_szer
button2y = 0.25*okno_dl

podstawowka = Button(root, text = 'Szkoła Podstawowa', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openpodst).place(x= button1x, y=button1y)
liceum = Button(root, text = 'Liceum', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openlo).place(x= button2x, y=button2y)

#dodanie zdjęcia u dołu strony dopasowanego do wymiarów okna aplikacji
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'learning.png')
learning = PhotoImage(file=image_path)

label = Label(image=learning, width = okno_dl, height = 0.43 * okno_szer)
label.image = learning
label.pack(side = BOTTOM)


root.mainloop()  