from random import *
import copy
from Vier_Gewinnt_Klasse import viergewinntklasse
class KI:
    def __init__(self,eigendeSpielsteinfarbe,fremdeSpielsteinfarbe):
        self.__Spielfeld = [["w" for x in range(7)] for y in range(6)]
        self.__eigeneSpielsteinfarbe = eigendeSpielsteinfarbe
        self.__fremdeSpielsteinfarbe = fremdeSpielsteinfarbe
        self.__Spielzug = None
        self.__VierGewinntKlasse = viergewinntklasse()

    def setSpielfeld(self,Spielfeld):
        self.__Spielfeld = copy.deepcopy(Spielfeld)



        # Überprüfung ob man selber 3 Steine in einer Reihe hat 
    def ÜberprüfungZugzumGewinn(self,Spieler,Gegner):
        #### Senkrecht
        zähler = 0
        for x in range(7):
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    break
            if zähler == 3:
                self.__Spielzug = x

        ##### Waagerecht
        zähler = 0
        position = None
        for y in range(6):
            leer = False
            for x in range(7):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    zähler = 0
                elif self.__Spielfeld[y][x] == "w":
                    if leer == False:
                        zähler+1
                        position = x
                        leer = True
                if zähler == 4:
                    self.__Spielzug = position

        #### Senkrecht
        
        for x in range(7):
            zähler = 0
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler or self.__Spielfeld[y][x] == Gegner:
                    y = y -1
                    position = x
                    schleife = True
                    while schleife: 
                        if y < 5 and x > 0:
                            y = y+1
                            x=x-1
                            if self.__Spielfeld[y][x] == Spieler:
                                zähler = zähler + 1
                            else:
                                break
                        else:
                            break

                    schleife = True
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
                    if zähler >= 4:
                        self.__Spielzug = position

                    else:
                        zähler = 0

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

                        if zähler >= 4:
                            self.__Spielzug = position


    def ÜberprüfungZugschlaulegen(self,Spieler,Gegner):
        #### Senkrecht
        zähler = 0
        eigenerSpielerenthalten = False
        for x in range(7):
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                    eigenerSpielerenthalten = True
                elif self.__Spielfeld[y][x] == "w":
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    break
            if zähler == 4 and eigenerSpielerenthalten == True:
                self.__Spielzug = x

        ##### Waagerecht
        zähler = 0
        position = None
        eigenerSpielerenthalten = False
        for y in range(6):
            leer = False
            for x in range(7):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 1
                    eigenerSpielerenthalten = True
                elif self.__Spielfeld[y][x] == "w":
                    zähler = zähler + 1
                    position = x
                elif self.__Spielfeld[y][x] == Gegner:
                    zähler = 0
                if zähler == 4 and eigenerSpielerenthalten == True:
                    self.__Spielzug = position

        #### Diagonal
        eigenerSpielerenthalten = False
        position = None
        for x in range(7):
            zähler = 0
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler or self.__Spielfeld[y][x] == Gegner:
                    y = y -1
                    position = x
                    schleife = True
                    while schleife: 
                        if y < 5 and x > 0:
                            y = y+1
                            x=x-1
                            if self.__Spielfeld[y][x] == Spieler:
                                zähler = zähler + 1
                                eigenerSpielerenthalten = True
                            elif self.__Spielfeld[y][x] == "w":
                                zähler = zähler + 1
                            else:
                                break
                        else:
                            break

                    schleife = True
                    while schleife: 
                        if y > 0 and x < 6:
                            y = y-1
                            x=x+1
                            if self.__Spielfeld[y][x] == Spieler:
                                zähler = zähler + 1
                                eigenerSpielerenthalten = True
                            elif self.__Spielfeld[y][x] == "w":
                                zähler = zähler + 1
                            else:
                                break
                        else:
                            break
                    if zähler >= 4 and eigenerSpielerenthalten == True:
                        self._Spielzug = position

                    else:
                        zähler = 0
                        eigenerSpielerenthalten=False
                        position = None
                        schleife = True
                        while schleife: 
                            if y < 5 and x < 6:
                                y = y+1
                                x=x+1
                                if self.__Spielfeld[y][x] == Spieler:
                                    zähler = zähler + 1
                                    eigenerSpielerenthalten = True
                                elif self.__Spielfeld[y][x] == "w":
                                    zähler = zähler + 1
                                else:
                                    break
                            else:
                                break
                        schleife = True
                        while schleife: 
                            if y > 0 and x > 0:
                                y = y-1
                                x=x-1
                                if self.__Spielfeld[y][x] == Spieler:
                                    zähler = zähler + 1
                                    eigenerSpielerenthalten = True
                                elif self.__Spielfeld[y][x] == "w":
                                    zähler = zähler + 1
                                else:
                                    break
                            else:
                                break

                        if zähler >= 4 and eigenerSpielerenthalten == True:
                            Self.__Spielzug = position



    def Spielzuggenerieren(self):
        self.__Spielzug = None
        # Überprüfung ob man den allererstenZug hat
        Array = [["w" for x in range(7)] for y in range(6)]
        if self.__Spielfeld == Array:
            # Aller erster Zug der Ki ist immer in der Mitte
            self.__Spielzug = 3
            return self.__Spielzug
        ## Überprüfung ob man selber gewinnen kann
        self.ÜberprüfungZugzumGewinn(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
        if self.__Spielzug != None:
            return self.__Spielzug
        else:
        ## Überprüfung ob Gegner gewinnen kann
            self.ÜberprüfungZugzumGewinn(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
            if self.__Spielzug != None:
                return self.__Spielzug
            else:
                self.ÜberprüfungZugschlaulegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
                if self.__Spielzug != None:
                    self.__VierGewinntKlasse._viergewinntklasse__Array = self.__Spielfeld
                    self.__VierGewinntKlasse.setSpielzug(self.__Spielzug)
                    self.__VierGewinntKlasse.ausführen()
                    if self.__VierGewinntKlasse.getErgebnis() == "":
                        return self.__Spielzug
        while True:
            self.__Spielzug = randint(0,6)
            # Überprüfung
            if self.__Spielfeld[0][self.__Spielzug] =="w":
                self.__VierGewinntKlasse._viergewinntklasse__Array = self.__Spielfeld
                self.__VierGewinntKlasse.setSpielzug(self.__Spielzug)
                self.__VierGewinntKlasse.ausführen()
                if self.__VierGewinntKlasse.getErgebnis() == "":
                    return self.__Spielzug









                




        