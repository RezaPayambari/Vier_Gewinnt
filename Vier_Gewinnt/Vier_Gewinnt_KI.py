from random import *
import copy
from Vier_Gewinnt_Klasse import viergewinntklasse
class KI:
    def __init__(self,eigendeSpielsteinfarbe,fremdeSpielsteinfarbe):
        self.__Spielfeld = [["w" for x in range(7)] for y in range(6)]
        self.__eigeneSpielsteinfarbe = eigendeSpielsteinfarbe
        self.__fremdeSpielsteinfarbe = fremdeSpielsteinfarbe
        self.__Spielzug = ""
        self.__VierGewinntKlasse = None

    def setSpielfeld(self,Spielfeld):
        self.__Spielfeld = copy.deepcopy(Spielfeld)



        # Überprüfung ob man selber 3 Steine in einer Reihe hat 
    def ÜberprüfungZugzumGewinn(self,Spieler,Gegner):
        self.ÜberprüfungZugzumGewinn_senkrecht(Spieler,Gegner)
        if self.__Spielzug =="":
            self.ÜberprüfungZugzumGewinn_waagerecht(Spieler,Gegner)
            if self.__Spielzug =="":
                self.ÜberprüfungZugzumGewinn_diagonal(Spieler,Gegner)


    def ÜberprüfungZugzumGewinn_senkrecht(self,Spieler,Gegner):
        #### Senkrecht
        
        for x in range(7):
            zähler = 0
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    break
            if zähler == 3:
                self.__Spielzug = x
                break

        ##### Waagerecht
        """ 
        funktioniert noch nicht
        x positionx muss besser ermittlet werden
        Idee: Wenn auf gelb splate minus eins feld dann überprüfen, wenn besetzt spalte plus 4
        """
    def ÜberprüfungZugzumGewinn_waagerecht(self,Spieler,Gegner):
        zähler = 0
        positionx = None
        psitiony = None
        for y in range(5,-1,-1):
            if self.__Spielzug != "":
                break
            leer = False
            zähler = 0
            for x in range(7):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    zähler = 0
                    leer = False
                elif self.__Spielfeld[y][x] == "w":
                    if leer == False:
                        zähler = zähler+1
                        positionx = x
                        positiony = y
                        leer = True
                    elif zähler >1:
                        positionx = x
                        positiony = y
                        #zähler = zähler + 1

                    else:
                        zähler = 1
                        positionx = x
                        positiony = y
                if zähler == 4:
                    if self.SinnvollerZug(positionx,positiony) == True:
                        self.__Spielzug = positionx
                        break
                    elif positionx + 4 <= 6 and self.__Spielfeld[positiony][positionx + 4] == "w":
                        if self.SinnvollerZug(positionx + 4,positiony) == True:
                            self.__Spielzug = positionx + 4
                            break


        #### Diagonal
    def ÜberprüfungZugzumGewinn_diagonal(self,Spieler,Gegner):
        for x1 in range(7):
            
            zähler = 0
            if self.__Spielzug != "":
                break
            for y1 in range(6):
                y = copy.deepcopy(y1)
                x = copy.deepcopy(x1)
                if self.__Spielfeld[y1][x1] == "w":
             #       y = y -1
                    Ursprungx = copy.deepcopy(x1)
                    Ursprungy = copy.deepcopy(y1)
                    positionx = copy.deepcopy(x1)
                    positiony = copy.deepcopy(y1)
                    schleife = True
                    while schleife: 
                        if y < 5 and x > 0:
                            y = y+1
                            x = x-1
                            if self.__Spielfeld[y][x] == Spieler:
                                zähler = zähler + 1
                            else:
                                break
                        else:
                            break

                    schleife = True
                    x = Ursprungx
                    y = Ursprungy
                    while schleife: 
                        if y > 0 and x < 6:
                            y = y-1
                            x=x+1
                            if self.__Spielfeld[y][x] == Spieler:
                                zähler = zähler + 1
                            else:
                                break
                        else:
                            break
                    if zähler >= 3:
                        if self.SinnvollerZug(positionx,positiony) == True:    
                            self.__Spielzug = positionx
                            break

                    else:
                        zähler = 0
                        x = Ursprungx
                        y = Ursprungy
                        schleife = True
                        while schleife: 
                            if y < 5 and x < 6:
                                y = y+1
                                x=x+1
                                if self.__Spielfeld[y][x] == Spieler:
                                    zähler = zähler + 1
                                else:
                                    break
                            else:
                                break
                        schleife = True
                        x = Ursprungx
                        y = Ursprungy
                        while schleife: 
                            if y > 0 and x > 0:
                                y = y-1
                                x=x-1
                                if self.__Spielfeld[y][x] == Spieler:
                                    zähler = zähler + 1
                                else:
                                    break
                            else:
                                break

                        if zähler >= 3:
                            if self.SinnvollerZug(positionx,positiony) == True:
                                self.__Spielzug = positionx
                                break


    #def ÜberprüfungZugschlaulegen(self,Spieler,Gegner):
    #    #### Senkrecht
    #    zähler = 0
    #    eigenerSpielerenthalten = False
    #    for x in range(7):
    #        for y in range(6):
    #            if self.__Spielfeld[y][x] == Spieler:
    #                zähler = zähler + 1
    #                eigenerSpielerenthalten = True
    #            elif self.__Spielfeld[y][x] == "w":
    #                zähler = zähler + 1
    #            elif self.__Spielfeld[y][x] == Gegner:
    #                break
    #        if zähler == 4 and eigenerSpielerenthalten == True:
    #            self.__Spielzug = x

    #    ##### Waagerecht
    #    zähler = 0
    #    positionx = None
    #    eigenerSpielerenthalten = False
    #    for y in range(6):
    #        leer = False
    #        for x in range(7):
    #            if self.__Spielfeld[y][x] == Spieler:
    #                zähler = zähler + 1
    #                eigenerSpielerenthalten = True
    #            elif self.__Spielfeld[y][x] == "w":
    #                zähler = zähler + 1
    #                positionx = x
    #            elif self.__Spielfeld[y][x] == Gegner:
    #                zähler = 0
    #            if zähler == 4 and eigenerSpielerenthalten == True:
    #                self.__Spielzug = positionx

    #    #### Diagonal
    #    eigenerSpielerenthalten = False
    #    positionx = None
    #    for x in range(7):
    #        zähler = 0
    #        for y in range(6):
    #            if self.__Spielfeld[y][x] == Spieler or self.__Spielfeld[y][x] == Gegner:
    #                y = y -1
    #                positionx = x
    #                schleife = True
    #                while schleife: 
    #                    if y < 5 and x > 0:
    #                        y = y+1
    #                        x=x-1
    #                        if self.__Spielfeld[y][x] == Spieler:
    #                            zähler = zähler + 1
    #                            eigenerSpielerenthalten = True
    #                        elif self.__Spielfeld[y][x] == "w":
    #                            zähler = zähler + 1
    #                        else:
    #                            break
    #                    else:
    #                        break

    #                schleife = True
    #                while schleife: 
    #                    if y > 0 and x < 6:
    #                        y = y-1
    #                        x=x+1
    #                        if self.__Spielfeld[y][x] == Spieler:
    #                            zähler = zähler + 1
    #                            eigenerSpielerenthalten = True
    #                        elif self.__Spielfeld[y][x] == "w":
    #                            zähler = zähler + 1
    #                        else:
    #                            break
    #                    else:
    #                        break
    #                if zähler >= 4 and eigenerSpielerenthalten == True:
    #                    self._Spielzug = positionx

    #                else:
    #                    zähler = 0
    #                    eigenerSpielerenthalten=False
    #                    positionx = None
    #                    schleife = True
    #                    while schleife: 
    #                        if y < 5 and x < 6:
    #                            y = y+1
    #                            x=x+1
    #                            if self.__Spielfeld[y][x] == Spieler:
    #                                zähler = zähler + 1
    #                                eigenerSpielerenthalten = True
    #                            elif self.__Spielfeld[y][x] == "w":
    #                                zähler = zähler + 1
    #                            else:
    #                                break
    #                        else:
    #                            break
    #                    schleife = True
    #                    while schleife: 
    #                        if y > 0 and x > 0:
    #                            y = y-1
    #                            x=x-1
    #                            if self.__Spielfeld[y][x] == Spieler:
    #                                zähler = zähler + 1
    #                                eigenerSpielerenthalten = True
    #                            elif self.__Spielfeld[y][x] == "w":
    #                                zähler = zähler + 1
    #                            else:
    #                                break
    #                        else:
    #                            break

    #                    if zähler >= 4 and eigenerSpielerenthalten == True:
    #                        self.__Spielzug = positionx

    def SinnvollerZug(self, Zug, Ebene = 10000):
        # überprüfung ob der Stein auch auf der richtigen Ebene landet
        if Ebene != 10000 and Ebene < 5:
            if self.__Spielfeld[int(Ebene)+1][Zug] == "w":
                return False
        
        # um sicherzugehen das man sich mit dem eigenen zug kein Grab schaufelt
        if self.__eigeneSpielsteinfarbe == "gr":
            reststeine = 20
        else:
            reststeine = 19
        spielfeld = copy.deepcopy(self.__Spielfeld)
        self.__VierGewinntKlasse = viergewinntklasse(spielfeld,reststeine)
        self.__VierGewinntKlasse.setSpielzug(Zug)
        self.__VierGewinntKlasse.ausführen()
        self.__VierGewinntKlasse.setSpielzug(Zug)
        self.__VierGewinntKlasse.ausführen()
        if self.__VierGewinntKlasse.getErgebnis() == self.__fremdeSpielsteinfarbe:
            return False
        else: 
            return True



    def Spielzuggenerieren(self):
        self.__Spielzug = ""
        # Überprüfung ob man den allererstenZug hat
        Array = [["w" for x in range(7)] for y in range(6)]
        # Aller erster Zug der Ki ist immer in der Mitte
        if self.__Spielfeld == Array:
            self.__Spielzug = 3
            return self.__Spielzug
        # Überprüfung ob man selber gewinnen kann
        self.ÜberprüfungZugzumGewinn(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob Gegner gewinnen kann und positionsermittlung um dies zuverhindern
        self.ÜberprüfungZugzumGewinn(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        x=0
        while True:
            x=x + 1
            self.__Spielzug = randint(0,6)
            #self.__Spielzug = 2
            # Überprüfung
            #   if self.__Spielzug ==0:
            #       print("Hallo")
            if self.SinnvollerZug(self.__Spielzug) == True or x == 1000:
                return self.__Spielzug # falsche Einrückung









                




        