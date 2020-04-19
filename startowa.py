from tkinter import *
from PIL import Image, ImageTk



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #stworzenie nowego okna
    def init_window(self):

        #nadanie tytułu      
        self.master.title("Platforma Edukacyjna")



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

tekst = Label(root, text = 'Wybierz etap edukacji:', font = "Arial 30 ", width = okno_szer, height=4,background='MistyRose3', fg = 'misty rose', anchor = CENTER)
tekst.pack()

root.configure(background='misty rose')

podstawowka = Button(root, text = 'Szkoła Podstawowa')
podstawowka.pack()
root.mainloop()  