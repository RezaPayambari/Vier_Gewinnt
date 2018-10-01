import pgzrun
from Vier_Gewinnt_Klasse import viergewinntklasse
import time


def draw():
    global Vier_Gewinnt
    global LabelListe


    # Hintergrund
    screen.fill("grey")
    # Spielsteine zeichnen (Grün, Gelb, Weiß)
    for Spieler in Spielerliste:
        Spieler.draw()
    # Label zeichen
    for Label in LabelListe:
        screen.draw.text(Label.gettext(), (Label.getxposition(), Label.getypsition()), color="white")
        
    screen.draw.text(str(Vier_Gewinnt.getSpielstandGelb()), (550, 500))
    screen.draw.text(str(Vier_Gewinnt.getSpielstandGruen()),( 550, 550))

    if Vier_Gewinnt.getSpielbeendet() == True:
        labelsetzen("Neues Match",20,540)
        labelsetzen("Neues Spiel",150,540)




# Methode fügt Daten (Text,xPosition,yPosition) für ein Label als Array in ein Array
def labelsetzen(text,xposition,yposition):
    Label = labelklasse(text,xposition,yposition)
    x=0
    for i in LabelListe:
        if i.gettext() == Label.gettext():
            x=1
    if x==0:
      LabelListe.append(Label)





def on_mouse_down(pos):
    global Vier_Gewinnt

    # Spalte des Zuges ermitteln
    xmouse = pos[0]
    ymouse = pos[1]
    spalte = 100
    if xmouse >= 2.5 and xmouse <= 67.4:
        spalte = 0
    elif xmouse >= 67.5 and xmouse <= 132.4:
        spalte = 1
    elif xmouse >= 132.5 and xmouse <= 197.4:
        spalte = 2
    elif xmouse >= 197.5 and xmouse <= 262.4:
        spalte = 3
    elif xmouse >= 152.5 and xmouse <= 327.4:
        spalte = 4
    elif xmouse >= 217.5 and xmouse <= 392.4:
        spalte = 5
    elif xmouse >= 272.5 and xmouse <= 457.4:
        spalte = 6
    if ymouse <= 4 or ymouse >= 395:
        spalte = 100
    if spalte != 100 and Vier_Gewinnt.getSpielbeendet() == False:
        Vier_Gewinnt.setSpielzug(spalte)
        Vier_Gewinnt.ausführen()
        # Spielfeld erstellen
        __Spielfeldgenerieren()
    # Label setzen wenn einer gewonnen hat
    if Vier_Gewinnt.getErgebnis() == "ge":
        labelsetzen("Spieler Gelb hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "gr":
        labelsetzen("Spieler Grün hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "un":
        labelsetzen("Unentschieden",10,500)


    # wenn Spielbeendet ist und ein neues Match starten soll
    if Vier_Gewinnt.getSpielbeendet() == True:
        g = False
        if xmouse >= 18 and xmouse <= 135 and ymouse >=540 and ymouse <=555:
            Vier_Gewinnt.neuesMatch()
            __Spielfeldgenerieren()
            g = True
        if xmouse >= 148 and xmouse <= 248 and ymouse >=538 and ymouse <=555:
            Vier_Gewinnt = viergewinntklasse()
            __Spielfeldgenerieren()
            g = True

        if g == True:
            for label in LabelListe:
                if str(label.gettext()) == "Spieler Gelb hat gewonnen." or str(label.gettext()) == "Spieler Grün hat gewonnen." or str(label.gettext()) == "Unentschieden":
                    label1 = label
                if str(label.gettext()) == "Neues Match":
                    label2 = label
                if str(label.gettext()) == "Neues Spiel":
                    label3 = label

            LabelListe.remove(label1)
            LabelListe.remove(label2)
            LabelListe.remove(label3)

    draw()

def __Spielfeldgenerieren():
    global Array
    Array = Vier_Gewinnt.getArray()
    xposition = 30
    yposition = 30
    for x in range(7):
        yposition = -30
        xposition = xposition +5
        for y in range(6):
            yposition = yposition +65
            if Array[y][x] == "w":
                Spieler = Actor("spieler_weiß")
            elif Array[y][x] == "ge":
                Spieler = Actor("spieler_gelb")
            elif Array[y][x] == "gr":
                Spieler = Actor("spieler_gruen")
            Spieler.x = xposition
            Spieler.y = yposition
            Spielerliste.append(Spieler)
        xposition = xposition + 60

    
class labelklasse:
    def __init__(self,text,xposition,yposition):
        self.__text = text
        self.__xposition = xposition
        self.__yposition = yposition

    def gettext(self):
        return self.__text

    def getxposition(self):
        return self.__xposition

    def getypsition(self):
        return self.__yposition


Vier_Gewinnt = viergewinntklasse()
HEIGHT = 600
WIDTH = 600


xposition = 30
yposition = 30
Spielerliste = []
LabelListe = []
Array = [["w" for x in range(7)] for y in range(6)]
# Leeres Spielfeld generieren
__Spielfeldgenerieren()
labelsetzen("Spielstand",400,450)
labelsetzen("Spieler Gelb :",400,500)
labelsetzen("Spieler Grün :",400,550)


pgzrun.go()

