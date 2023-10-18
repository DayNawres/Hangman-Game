from tkinter import *
import tkinter.font as font


class Joueur(object):
    def __init__(self, selfOfPenduClass):

        self.fen = Tk()
        self.f = font.Font(family='Time New Roman', size=20)
        self.fen.geometry("600x400")
        self.fen.configure(bg='#E7E7E7')
        self.fen.title("C'est le jeu de pendule !")
        self.ch3 = Label(self.fen)
        self.ch3['font'] = self.f
        self.but = Button(self.fen, text="Sortir",
                          command=self.fen.quit, bg="#d46c4e")
        self.but['font'] = self.f
        self.ch3.configure(text="Veuillez entrer un mot !", bg="#7097AB")
        self.ch3.pack()
        self.entre = Entry(self.fen, show="_")  # mot a deviner
        self.entre['font'] = self.f
        self.lettre = Entry(self.fen)  # lettre donné
        self.ch1 = Label(self.fen)
        self.entre.bind("<Return>", selfOfPenduClass.change_mot)

        self.entre.pack()
        self.ch1.pack()

        self.ch4 = Label(self.fen)
        self.ch4.configure(text="Veuillez entrer une lettre !", bg="#7097AB")
        self.ch4['font'] = self.f
        self.ch4.pack()
        self.lettre.bind("<Return>", selfOfPenduClass.test)

        self.lettre.pack()

        self.ch2 = Label(self.fen)

        self.ch2.pack()

        self.ch5 = Label(self.fen)

        self.ch5.pack()

        self.ch6 = Label(self.fen)

        self.ch6.pack()

        self.ch7 = Label(self.fen)

        self.ch7.pack()

        self.but.pack()

    def get_mot(self):
        return self.entre.get()

    def get_lettre(self):
        return self.lettre.get()

    def run(self):
        self.fen.mainloop()
