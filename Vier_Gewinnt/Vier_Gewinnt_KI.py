from random import *
import copy
from Vier_Gewinnt_Klasse import viergewinntklasse
class KI:
    def __init__(self,eigendeSpielsteinfarbe,fremdeSpielsteinfarbe):
        self.__Spielfeld = [["w" for x in range(7)] for y in range(6)]
        self.__eigeneSpielsteinfarbe = eigendeSpielsteinfarbe
        self.__fremdeSpielsteinfarbe = fremdeSpielsteinfarbe
        self.__Spielzug = ""
        self.__VierGewinntKlasse = viergewinntklasse()

    def setSpielfeld(self,Spielfeld):
        self.__Spielfeld = copy.deepcopy(Spielfeld)



        # Überprüfung ob man selber 3 Steine in einer Reihe hat 
    def ÜberprüfungZugzumGewinn(self,Spieler,Gegner):
     #   self.ÜberprüfungZugzumGewinn_senkrecht(Spieler,Gegner)
      #  if self.__Spielzug =="":
       #     self.ÜberprüfungZugzumGewinn_waagerecht(Spieler,Gegner)
        #    if self.__Spielzug =="":
        self.ÜberprüfungZugzumGewinn_diagonal(Spieler,Gegner)


    def ÜberprüfungZugzumGewinn_senkrecht(self,Spieler,Gegner):
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
                break

        ##### Waagerecht
        """ 
        funktioniert noch nicht
        x position muss besser ermittlet werden
        Idee: Wenn auf gelb splate minus eins feld dann überprüfen, wenn besetzt spalte plus 4
        """
    def ÜberprüfungZugzumGewinn_waagerecht(self,Spieler,Gegner):
        zähler = 0
        position = None
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
                elif self.__Spielfeld[y][x] == "w":
                    if leer == False:
                        zähler = zähler+1
                        position = x
                        leer = True
                    elif zähler >1:
                        position = x

                    else:
                        zähler = 1
                        position = x
                if zähler == 4:
                    self.__Spielzug = position
                    break

        #### Diagonal
    def ÜberprüfungZugzumGewinn_diagonal(self,Spieler,Gegner):
        for x in range(7):
            zähler = 0
            if self.__Spielzug != "":
                break
            for y in range(6):
                if self.__Spielfeld[y][x] == "w":
             #       y = y -1
                    Ursprungx = copy.deepcopy(x)
                    Ursprungy = copy.deepcopy(y)
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
                        self.__Spielzug = position
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
                            self.__Spielzug = position
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
    #    position = None
    #    eigenerSpielerenthalten = False
    #    for y in range(6):
    #        leer = False
    #        for x in range(7):
    #            if self.__Spielfeld[y][x] == Spieler:
    #                zähler = zähler + 1
    #                eigenerSpielerenthalten = True
    #            elif self.__Spielfeld[y][x] == "w":
    #                zähler = zähler + 1
    #                position = x
    #            elif self.__Spielfeld[y][x] == Gegner:
    #                zähler = 0
    #            if zähler == 4 and eigenerSpielerenthalten == True:
    #                self.__Spielzug = position

    #    #### Diagonal
    #    eigenerSpielerenthalten = False
    #    position = None
    #    for x in range(7):
    #        zähler = 0
    #        for y in range(6):
    #            if self.__Spielfeld[y][x] == Spieler or self.__Spielfeld[y][x] == Gegner:
    #                y = y -1
    #                position = x
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
    #                    self._Spielzug = position

    #                else:
    #                    zähler = 0
    #                    eigenerSpielerenthalten=False
    #                    position = None
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
    #                        self.__Spielzug = position



    def Spielzuggenerieren(self):
        self.__Spielzug = ""
        # Überprüfung ob man den allererstenZug hat
        Array = [["w" for x in range(7)] for y in range(6)]
        # Aller erster Zug der Ki ist immer in der Mitte
        if self.__Spielfeld == Array:
            self.__Spielzug = 3
            return self.__Spielzug
        ## Überprüfung ob man selber gewinnen kann
      #  self.ÜberprüfungZugzumGewinn(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
       # if self.__Spielzug != "":
       #     return self.__Spielzug
      #  else:
        ## Überprüfung ob Gegner gewinnen kann und Positionsermittlung um dies zuverhindern
        self.ÜberprüfungZugzumGewinn(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug
    #    else:
   #         self.ÜberprüfungZugschlaulegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
    #        if self.__Spielzug != "":
     #           self.__VierGewinntKlasse._viergewinntklasse__Array = self.__Spielfeld
      #          self.__VierGewinntKlasse.setSpielzug(self.__Spielzug)
       #         self.__VierGewinntKlasse.ausführen()
        #        if self.__VierGewinntKlasse.getErgebnis() == "":
         #           return self.__Spielzug
        else:
            while True:
                self.__Spielzug = randint(0,6)
                #self.__Spielzug = 6
                # Überprüfung
                #if self.__Spielfeld[0][self.__Spielzug] =="w":
           #         self.__VierGewinntKlasse._viergewinntklasse__Array = self.__Spielfeld
            #        self.__VierGewinntKlasse.setSpielzug(self.__Spielzug)
             #       self.__VierGewinntKlasse.ausführen()
              #      if self.__VierGewinntKlasse.getErgebnis() == "":
                return self.__Spielzug # falsche Einrückung









                




        