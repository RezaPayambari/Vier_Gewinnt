

class viergewinntklasse:
    def __init__(self):
        self.__Array = [["w" for x in range(7)] for y in range(6)]
        self.__RestSpielzüge = 43
        self.__Ergebnis = ""
        self.__Spielzug = ""
        self.__SpielstandGruen = 0
        self.__SpielstandGelb = 0
        self.__Spielbeendet = False

    def getSpielbeendet(self):
        return self.__Spielbeendet

    def getSpielstandGruen(self):
        return self.__SpielstandGruen

    def getSpielstandGelb(self):
        return self.__SpielstandGelb

    def getArray(self):
        return self.__Array

    def getErgebnis(self):
        return self.__Ergebnis

    def setSpielzug(self,spalte):
        if spalte < 7 and spalte >= 0:
            self.__Spielzug = spalte

    def ausführen(self):
        self.__Spielzugübertragung()
        self.__Spielergebnis()

    def neuesMatch(self):
        self.__Array = [["w" for x in range(7)] for y in range(6)]
        self.__RestSpielzüge = 43
        self.__Ergebnis = ""
        self.__Spielzug = ""
        self.__Spielbeendet = False

    def __Spielergebnis(self):
        self.__diagonaleÜberprüfung()
        self.__senkrechteÜberprüfung()
        self.__waagerechteÜberprüfung()
        if self.__Ergebnis == "" and self.__RestSpielzüge == 1:
            self.__Ergebnis = "un"
            self.__Spielbeendet = True
        elif self.__Ergebnis !="":
            self.__Spielbeendet = True
        if self.__Ergebnis == "ge":
            self.__SpielstandGelb = self.__SpielstandGelb +1
        elif self.__Ergebnis =="gr":
            self.__SpielstandGruen = self.__SpielstandGruen +1

    def __diagonaleÜberprüfung(self):
        # linksoben nach rechts unten
        for i in range(0,4):
            x=i
            zählerSpielergruen = 0
            zählerSpielergelb = 0
            for y in range (6):
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0
                if x < 6:
                    x = x+1

            

            

        for i in range(1,3):
            y=i
            zählerSpielergruen = 0
            zählerSpielergelb = 0
            for x in range (5):
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0
                if y < 5:
                    y = y+1

            
        
        # linksunten nach rechtsoben
        for i in range(0,4):
            x=i
            zählerSpielergruen = 0
            zählerSpielergelb = 0
            y=5
            while y>=0:
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0
                y=y-1
                if x < 6:
                    x = x+1

            
                

        i=0
        for i in range(4,2,-1):
            y=i
            zählerSpielergruen = 0
            zählerSpielergelb = 0
            for x in range (6):
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0
                if y >=0:
                    y = y-1


       



    def __senkrechteÜberprüfung(self):

        for x in range(7):
            zählerSpielergelb = 0
            zählerSpielergruen = 0
            for y in range(6):
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"#
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0

    
    def __waagerechteÜberprüfung(self):

        for y in range(6):
            zählerSpielergelb = 0
            zählerSpielergruen = 0
            for x in range(7):
                if self.__Array[y][x] =="ge":
                    zählerSpielergelb = zählerSpielergelb+1
                    zählerSpielergruen = 0
                    if zählerSpielergelb == 4:
                        self.__Ergebnis = "ge"
                        break
                elif self.__Array[y][x] == "gr":
                    zählerSpielergruen = zählerSpielergruen+1
                    zählerSpielergelb = 0
                    if zählerSpielergruen == 4:
                        self.__Ergebnis = "gr"
                        break
                elif self.__Array[y][x] == "w":
                    zählerSpielergruen = 0
                    zählerSpielergelb = 0

    def __Spielzugübertragung(self):
        # Spieler Gelb
        y = 0
        while self.__Array[y][int(self.__Spielzug)] == "w":
            y=y+1
            if y==6:
                break
        if y>0:
            if self.__RestSpielzüge%2 ==1:
                self.__Array[y-1][int(self.__Spielzug)] = "ge"
            elif self.__RestSpielzüge%2 ==0:
                self.__Array[y-1][int(self.__Spielzug)] = "gr"
            self.__RestSpielzüge = self.__RestSpielzüge-1
        
