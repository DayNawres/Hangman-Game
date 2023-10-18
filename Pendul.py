from graphics import Joueur

class Pendu:
    def __init__(self):
        self.joueur = Joueur(self)
        self.__mot = self.joueur.entre.get()
        self.__longmot = len(self.__mot)
        self.__essaye = ""  # chaine contienne la combinaison des lettres et des tirrets et sera mis a jour a chaque execution
        self.__nbr = 0
        self.joueur.run()

    def get_devinette(self):
        return self.__mot


    def get_number(self):
        return self.__nbr

    def get_unessaie(self):
        return self.__essaye

    def change_mot(self,event):
        mot=self.joueur.entre.get()
        for i in range(len(mot)):
            if ord(mot[i].upper()) not in range(65, 91):
                self.joueur.ch1.configure(text="C'est un erreur,réssayer!",bg="red")
                self.change_mot(event)
        self.joueur.ch1.configure(text="bien reçu",bg="green")
        self.__mot = mot
        self.__essaye = '_' * len(self.__mot)
        self.__nbr=0

    def changer_essaie(self, ch):
        self.__essaye=ch

    def changer_nbr(self):
        self.__nbr = self.__nbr + 1

    def affichage_mot(self, t):
        mot = self.get_devinette()
        ch = self.get_unessaie()
        for j in range(len(mot)):
            if mot[j] == t:
                ch = ch[0:j] + t + ch[j + 1:len(ch)]  # erreur d'affectation
        self.changer_essaie(ch)
        return ch

    def test(self, event):
        b = False
        t = " "
        x = self.joueur.lettre.get()
        if len(x) != 1 or ord(x[0].upper()) not in range(65, 91):
            self.joueur.ch2.configure(text="Il faut tapez une seule lettre !!!", bg="red")
            self.test(event)
        else:
            self.joueur.ch2.configure(text="bien reçu", bg="green")
            mot = self.get_devinette()
            for i in range(len(mot)):
                if x == mot[i]:
                    b = True
                    t = mot[i]

            if b == False:
                self.changer_nbr()
            a = self.get_number()
            affichage(a,self.joueur)
            self.joueur.ch6.configure(text=""+self.affichage_mot(t))
            if (self.__mot==self.__essaye):
                self.joueur.ch7.configure(text="Bravooo vous êtes un gagnant ")



def affichage(a,joueur):
    if a == 0:
        #joueur.chaine5.configure(text="a= "+str(a))
        joueur.ch5.configure(text=" ____ \n | \n | \n | \n | \n | \n",justify="left")
    elif a == 1:
        joueur.ch5.configure(text=" ____ \n |  |\n | \n | \n | \n | \n",justify="left")
    elif a == 2:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n | \n | \n | \n",justify="left")
    elif a == 3:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n |  |  \n | \n | \n", justify="left")
    elif a == 4:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n | /| \n | \n | \n", justify="left")
    elif a == 5:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n | /|\ \n | \n | \n", justify="left")
    elif a == 6:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n | /|\ \n | /   \n | \n", justify="left")
    elif a == 7:
        joueur.ch5.configure(text=" ____ \n |  |\n |  o\n | /|\ \n | / \ \n | \n Malheureusement vous êtes pendu ! \n", justify="left")
    joueur.ch7.configure(text="il vous reste "+str( 7 - a)+ " essais")

    

if __name__ == "__main__":
    x = Pendu()
