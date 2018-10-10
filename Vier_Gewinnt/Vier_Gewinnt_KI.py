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
    def __ÜberprüfungobdreiSteineineinerReiheliegen(self,Spieler,Gegner):
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner, 61)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,61)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,3)

    # Überprüfung ob zwei Steine in einer Reihe liegen und dann daneben legen, um Zwickmühlen zuverhindern
    def __ÜberprüfungobzweiSteineineinerReiheliegen(self,Spieler,Gegner):
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,42)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,2)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner,42)


        # Überprüfung ob ein Stein in einer Reihe liegt, damit der zug nicht komplet zufällig ist
    def __ÜberprüfungobeinSteineineinerReiheliegt(self,Spieler,Gegner):
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,23)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,1)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner, 23)



    def __ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(self,Spieler,Gegner, PunktefuerZug):
        #### Senkrecht
        
        for x in range(7):
            zähler = 0
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 20
                if self.__Spielfeld[y][x] == "w":
                    zähler = zähler + 1
                elif self.__Spielfeld[y][x] == Gegner:
                    break
            if zähler >= PunktefuerZug:
                self.__Spielzug = x
                break

        ##### Waagerecht

    def __ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(self,Spieler,Gegner, PunktefuerZug):
        Felderaddieren = 0
        if PunktefuerZug == 61:
            Felderaddieren = 4
        elif PunktefuerZug == 42:
            Felderaddieren = 3
        elif PunktefuerZug == 23:
            Felderaddieren = 2

        for y in range(5,-1,-1):
            if self.__Spielzug != "":
                break
            positionx = None
            psitiony = None
            weißenthalten = False
            zähler = 0
            for x in range(7):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 20
                elif self.__Spielfeld[y][x] == Gegner:
                    zähler = 0
                    weißenthalten = False
                elif self.__Spielfeld[y][x] == "w":
                    zähler = zähler + 1
                    weißenthalten = True
                    if zähler <= 20 or zähler == 61 or zähler == 42 or zähler == 23 or zähler == PunktefuerZug-1 or zähler == PunktefuerZug-2 or zähler+19:
                        positionx = x
                        positiony = y
                if zähler >= PunktefuerZug and weißenthalten == True:
                    if self.SinnvollerZug(positionx,positiony) == True:
                        self.__Spielzug = positionx
                        break
                    elif positionx + Felderaddieren <= 6 and self.__Spielfeld[positiony][positionx + Felderaddieren] == "w":
                        if self.SinnvollerZug(positionx + Felderaddieren,positiony) == True:
                            self.__Spielzug = positionx + Felderaddieren
                            break


        #### Diagonal
    def __ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(self,Spieler,Gegner,PunktefuerZug):
        for x1 in range(7):
            
            
            if self.__Spielzug != "":
                break
            for y1 in range(6):
                zähler = 0
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
                    if zähler >= PunktefuerZug:
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

                        if zähler >= PunktefuerZug:
                            if self.SinnvollerZug(positionx,positiony) == True:
                                self.__Spielzug = positionx
                                break


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
        Array = copy.deepcopy(self.__Spielfeld)
        self.__Spielfeld = copy.deepcopy(self.__VierGewinntKlasse.getArray())
        self.__ÜberprüfungobdreiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
        self.__Spielfeld = copy.deepcopy(Array)
        self.__VierGewinntKlasse.setSpielzug(Zug)
        self.__VierGewinntKlasse.ausführen()
        if self.__VierGewinntKlasse.getErgebnis() == self.__fremdeSpielsteinfarbe or self.__Spielzug == Zug:
            return False
        else: 
            # Überprüfung ob man sich selber verbauen kann
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
        self.__ÜberprüfungobdreiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob Gegner gewinnen kann und positionsermittlung um dies zuverhindern
        self.__ÜberprüfungobdreiSteineineinerReiheliegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob der Gegner zwei Steine in einer Zeile hat
        self.__ÜberprüfungobzweiSteineineinerReiheliegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob man selber zwei Steine in einer Zeile hat
        self.__ÜberprüfungobzweiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe, self.__fremdeSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Damit es nicht komplett zufällig wird
        self.__ÜberprüfungobeinSteineineinerReiheliegt(self.__eigeneSpielsteinfarbe, self.__fremdeSpielsteinfarbe)
        if self.__Spielzug != "":
            return self.__Spielzug


        # Wenn alles versagt hilft nur noch der Zufall
        x=0
        while True:
            x=x + 1
            self.__Spielzug = randint(0,6)
            # Überprüfung
            if self.SinnvollerZug(self.__Spielzug) == True or x == 1000:
                return self.__Spielzug









                




        