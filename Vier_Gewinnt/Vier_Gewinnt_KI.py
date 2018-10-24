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
    def ÜberprüfungobdreiSteineineinerReiheliegen(self,Spieler,Gegner,Überprüfung):
        if Überprüfung == None:
            Überprüfung = True
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner, 61,False)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,61,False)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,3,False)

    # Überprüfung ob zwei Steine in einer Reihe liegen und dann daneben legen, um Zwickmühlen zuverhindern
    def __ÜberprüfungobzweiSteineineinerReiheliegen(self,Spieler,Gegner,Überprüfung):
        if Überprüfung == None:
            Überprüfung = True
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,42,Überprüfung)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,2,Überprüfung)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner,42,Überprüfung)


        # Überprüfung ob ein Stein in einer Reihe liegt, damit der zug nicht komplet zufällig ist
    def __ÜberprüfungobeinSteineineinerReiheliegt(self,Spieler,Gegner,Überprüfung):
        if Überprüfung == None:
            Überprüfung = True
        self.__ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(Spieler,Gegner,23,Überprüfung)
        if self.__Spielzug =="":
            self.__ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(Spieler,Gegner,1,Überprüfung)
            if self.__Spielzug =="":
                self.__ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(Spieler,Gegner, 23,Überprüfung)



    def __ÜberprüfungwievieleSteineineinerReiheliegen_senkrecht(self,Spieler,Gegner, PunktefuerZug,Zugüberprüfung):
        #### Senkrecht
        
        for x in range(7):
            zähler = 0
            ebene = 0
            weißenthalten = False
            for y in range(6):
                if self.__Spielfeld[y][x] == Spieler:
                    zähler = zähler + 20
                if self.__Spielfeld[y][x] == "w":
                    zähler = zähler + 1
                    weißenthalten = True
                    ebene = y
                elif self.__Spielfeld[y][x] == Gegner:
                    break
            if zähler >= PunktefuerZug and weißenthalten == True:
                if self.SinnvollerZug(x,Zugüberprüfung,ebene) == True:
                    self.__Spielzug = x
                    break

        ##### Waagerecht

    def __ÜberprüfungwievieleSteineineinerReiheliegen_waagerecht(self,Spieler,Gegner, PunktefuerZug,Zugüberprüfung):
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
            positiony = None
            weißenthalten = False
            variable5 = True
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
               #     if (zähler <= 20 or zähler == 61 or zähler == 42 or zähler == 23 or zähler == PunktefuerZug-1 or zähler == PunktefuerZug-2) and variable5 == True:
                    if variable5 == True:
                        # abfrage wird benötigt um sicherzugehen, dass der Stein direkt neben dem bereits bestehenden Stein liegt
                        if zähler >= 20:
                            variable5 = False
                        positionx = x
                        positiony = y
                if zähler >= PunktefuerZug and zähler <= PunktefuerZug+5 and weißenthalten == True:
                    if self.SinnvollerZug(positionx,Zugüberprüfung,positiony) == True:
                        self.__Spielzug = positionx
                        break
                    elif positionx + Felderaddieren <= 6 and self.__Spielfeld[positiony][positionx + Felderaddieren] == "w":
                        if self.SinnvollerZug(positionx + Felderaddieren,Zugüberprüfung,positiony) == True:
                            self.__Spielzug = positionx + Felderaddieren
                            break


        #### Diagonal
    def __ÜberprüfungwievieleSteineineinerReiheliegen_diagonal(self,Spieler,Gegner,PunktefuerZug,zugüberprüfung):
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
                        if self.SinnvollerZug(positionx,zugüberprüfung,positiony) == True:    
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
                            if self.SinnvollerZug(positionx,zugüberprüfung,positiony) == True:
                                self.__Spielzug = positionx
                                break


    def SinnvollerZug(self, Zug,zugüberprüfung, Ebene):
        # überprüfung ob der Stein auch auf der richtigen Ebene landet
        if Zug == None:
            return False
        #if Ebene == 0 or Ebene == None or Ebene == 10000:
        if Ebene == None or Ebene == 10000:
            Ebene = 10000
            if self.__Spielfeld[int(0)][Zug] != "w":
                return False
        if Ebene != 10000 and Ebene < 5:
            if self.__Spielfeld[int(Ebene)+1][Zug] == "w":
                return False
            elif zugüberprüfung == False:
                return True
        if zugüberprüfung == True:
            # um sicherzugehen das man sich mit dem eigenen zug kein Grab schaufelt
            if self.__eigeneSpielsteinfarbe == "gr":
                reststeine = 20
            else:
                reststeine = 19
            spielfeld = copy.deepcopy(self.__Spielfeld)
            self.__VierGewinntKlasse = viergewinntklasse(spielfeld,reststeine)
            self.__VierGewinntKlasse.setSpielzug(Zug)
            self.__VierGewinntKlasse.ausführen()
            # Überprüfung ob man mit dem übernächsten zug gewinnen kann
            testKI = KI(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe)
            testKI.setSpielfeld(self.__VierGewinntKlasse.getArray())
            testKI.ÜberprüfungobdreiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe,False)
            testKIZug = testKI.__Spielzug
            """ Idee"""
       #     if self.__VierGewinntKlasse.getErgebnis != "":
        #        testgegnerKI = KI(self.__fremdeSpielsteinfarbe,self.__eigeneSpielsteinfarbe)
         #       testgegnerKI.setSpielfeld(self.__VierGewinntKlasse.getArray())
          #      testgegnerZug = testKI.Spielzuggenerieren(True)
            """ Test """
            testgegnerZug = Zug
            if testgegnerZug != None:
                self.__VierGewinntKlasse.setSpielzug(testgegnerZug)
                self.__VierGewinntKlasse.ausführen()
            else:
                return False
            if self.__VierGewinntKlasse.getErgebnis() == self.__fremdeSpielsteinfarbe or testKIZug != "":
                return False
            else: 
                # Überprüfung ob man sich selber verbauen kann
                return True
        else:
            return True


    def Spielzuggenerieren(self,Zugüberprüfung = None):
        self.__Spielzug = ""
        # Überprüfung ob man den allererstenZug hat
        Array = [["w" for x in range(7)] for y in range(6)]
        # Aller erster Zug der Ki ist immer in der Mitte
        if self.__Spielfeld == Array:
            self.__Spielzug = 3
            return self.__Spielzug
        # Überprüfung ob man selber gewinnen kann
        self.ÜberprüfungobdreiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe,self.__fremdeSpielsteinfarbe,Zugüberprüfung)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob Gegner gewinnen kann und positionsermittlung um dies zuverhindern
        self.ÜberprüfungobdreiSteineineinerReiheliegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe,Zugüberprüfung)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob der Gegner zwei Steine in einer Zeile hat
        self.__ÜberprüfungobzweiSteineineinerReiheliegen(self.__fremdeSpielsteinfarbe, self.__eigeneSpielsteinfarbe,Zugüberprüfung)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Überprüfung ob man selber zwei Steine in einer Zeile hat
        self.__ÜberprüfungobzweiSteineineinerReiheliegen(self.__eigeneSpielsteinfarbe, self.__fremdeSpielsteinfarbe,Zugüberprüfung)
        if self.__Spielzug != "":
            return self.__Spielzug

        # Damit es nicht komplett zufällig wird
        self.__ÜberprüfungobeinSteineineinerReiheliegt(self.__eigeneSpielsteinfarbe, self.__fremdeSpielsteinfarbe,Zugüberprüfung)
        if self.__Spielzug != "":
            return self.__Spielzug
        

        # Wenn alles versagt hilft nur noch der Zufall
        x=0
        while True:
            x=x + 1
            self.__Spielzug = randint(0,6)
       #     y1 = 0
        #    for y in range(0,6):
         #       if self.__Spielfeld[y][self.__Spielzug] != "w":
          #          break
           #     y1 = y
            # Überprüfung
            if self.SinnvollerZug(self.__Spielzug,True,10000) == True:
                return self.__Spielzug
            if x >= 1000:
                if self.SinnvollerZug(self.__Spielzug,False,10000) == True:
                    return self.__Spielzug









                




        