import pgzrun
from Vier_Gewinnt_Klasse import viergewinntklasse
import time
from Vier_Gewinnt_KI import KI
import sys
from Vier_Gewinnt_KI_2 import VierGewinnt_KI_2




def update():
    if (Spieler_Gelb_1_0 == True and Spieler_Gruen_1_0 == True)or (Spieler_Gelb_2_0 == True and Spieler_Gruen_1_0 == True)or(Spieler_Gelb_1_0 == True and Spieler_Gruen_2_0 == True)or(Spieler_Gelb_2_0 == True and Spieler_Gruen_2_0 == True):
        zweiKIsSpielen()
        __Spielfeldgenerieren()


        # Label setzen wenn einer gewonnen hat
    if Vier_Gewinnt.getErgebnis() == "ge":
        labelsetzen("Spieler Gelb hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "gr":
        labelsetzen("Spieler Grün hat gewonnen.",10,500)
    elif Vier_Gewinnt.getErgebnis() == "un":
        labelsetzen("Unentschieden",10,500)


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

   # if Spielbeginnt == False:


def zweiKIsSpielen():
    global Spieler_Gelb_1_0
    global Spieler_Gruen_1_0
    global Spieler_Gelb_2_0
    global Spieler_Gruen_2_0
    # ===============================================================================================================================================================================================================================
    if Vier_Gewinnt.getRestSpielzüge() %2 == 0 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gruen_1_0 == True:
        KI_Gruen_1_0.setSpielfeld(Array)
        Vier_Gewinnt.setSpielzug(KI_Gruen_1_0.Spielzuggenerieren())
        time.sleep(1)
        Vier_Gewinnt.ausführen()
    # ================================================================================================================================================================================================================================
        
    # ===============================================================================================================================================================================================================================
    elif Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_1_0 == True:
        KI_Gelb_1_0.setSpielfeld(Array)
        Vier_Gewinnt.setSpielzug(KI_Gelb_1_0.Spielzuggenerieren())
        time.sleep(1)
        Vier_Gewinnt.ausführen()
    # ================================================================================================================================================================================================================================
    
    
    # ===============================================================================================================================================================================================================================
    if Vier_Gewinnt.getRestSpielzüge() %2 == 0 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gruen_2_0 == True:
        KI_Gruen_2_0.setSpielfeld(Array)
        Vier_Gewinnt.setSpielzug(KI_Gruen_2_0.Spielzuggenerieren())
        time.sleep(1)
        Vier_Gewinnt.ausführen()
    # ================================================================================================================================================================================================================================
        
    # ===============================================================================================================================================================================================================================
    elif Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_2_0 == True:
        KI_Gelb_2_0.setSpielfeld(Array)
        Vier_Gewinnt.setSpielzug(KI_Gelb_2_0.Spielzuggenerieren())
        time.sleep(1)
        Vier_Gewinnt.ausführen()
    # ================================================================================================================================================================================================================================
  


# Methode fügt Daten (Text,xPosition,yPosition) für ein Label als Array in ein Array
def labelsetzen(text,xposition,yposition):
    Label = labelklasse(text,xposition,yposition)
    x=0
    for i in LabelListe:
        if i.gettext() == Label.gettext():
            x=1
    if x==0:
      LabelListe.append(Label)

def labelloeschen(text):
    label1 = None
    for label in LabelListe:
        if str(label.gettext()) == text:
            label1 = label
    if label1 != None:
        LabelListe.remove(label1)

def on_mouse_down(pos):
    global Vier_Gewinnt
    global Spielbeginnt
    global Spieler_Gelb_1_0
    global Spieler_Gruen_1_0
    global Spieler_Gelb_2_0
    global Spieler_Gruen_2_0
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
    if spalte != 100 and Vier_Gewinnt.getSpielbeendet() == False and Spielbeginnt == True:

        if Spieler_Gelb_1_0 == True and Vier_Gewinnt.getRestSpielzüge() %2 == 0 and Spieler_Gruen_1_0 == False:
            Vier_Gewinnt.setSpielzug(spalte)
            Vier_Gewinnt.ausführen()
        elif Spieler_Gruen_1_0 == True and Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Spieler_Gelb_1_0 == False:
            Vier_Gewinnt.setSpielzug(spalte)
            Vier_Gewinnt.ausführen()


        # ===============================================================================================================================================================================================================================
        if Vier_Gewinnt.getRestSpielzüge() %2 == 0 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gruen_1_0 == True and Spieler_Gelb_1_0 == False :
            KI_Gruen_1_0.setSpielfeld(Array)
            Vier_Gewinnt.setSpielzug(KI_Gruen_1_0.Spielzuggenerieren())
            time.sleep(1)
            Vier_Gewinnt.ausführen()
        # ================================================================================================================================================================================================================================

        # ===============================================================================================================================================================================================================================
        if Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_1_0 == True and Spieler_Gruen_1_0 == False:
            KI_Gelb_1_0.setSpielfeld(Array)
            Vier_Gewinnt.setSpielzug(KI_Gelb_1_0.Spielzuggenerieren())
            time.sleep(1)
            Vier_Gewinnt.ausführen()
        # ================================================================================================================================================================================================================================
        # Spielfeld erstellen


        # ===============================================================================================================================================================================================================================
        if Vier_Gewinnt.getRestSpielzüge() %2 == 0 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gruen_2_0 == True and Spieler_Gelb_1_0 == False and Spieler_Gelb_2_0 == False :
            KI_Gruen_2_0.setSpielfeld(Array)
            Vier_Gewinnt.setSpielzug(KI_Gruen_2_0.Spielzuggenerieren())
            time.sleep(1)
            Vier_Gewinnt.ausführen()
        # ================================================================================================================================================================================================================================

        # ===============================================================================================================================================================================================================================
        if Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_2_0 == True and Spieler_Gruen_1_0 == False and Spieler_Gruen_2_0 == False:
            KI_Gelb_2_0.setSpielfeld(Array)
            Vier_Gewinnt.setSpielzug(KI_Gelb_2_0.Spielzuggenerieren())
            time.sleep(1)
            Vier_Gewinnt.ausführen()
        # ================================================================================================================================================================================================================================
     



        __Spielfeldgenerieren()

    elif Spielbeginnt == False:
        # Spieler 1
        if xmouse >= 500 and xmouse <= 565 and ymouse >=100 and ymouse <=115:
            Spieler_Gelb_1_0 = False
            Spieler_Gelb_2_0 = False
        elif xmouse >= 600 and xmouse <= 615 and ymouse >=100 and ymouse <=115:
            Spieler_Gelb_1_0 = True
            Spieler_Gelb_2_0 = False
        elif xmouse >= 650 and xmouse <= 680 and ymouse >= 100 and ymouse <= 115:
            Spieler_Gelb_2_0 = True
            Spieler_Gelb_1_0 = False
        # Spieler 2
        if xmouse >= 500 and xmouse <= 565 and ymouse >=250 and ymouse <=265:
            Spieler_Gruen_1_0 = False
            Spieler_Gruen_2_0 = False
        elif xmouse >= 600 and xmouse <= 615 and ymouse >=250 and ymouse <=265:
            Spieler_Gruen_1_0 = True
            Spieler_Gruen_2_0 = False
        elif xmouse >= 650 and xmouse <= 680 and ymouse >=250 and ymouse <=265:
            Spieler_Gruen_2_0 = True
            Spieler_Gruen_1_0 = False

        if Spieler_Gelb_1_0 == True:
            labelloeschen("Mensch  ")
            labelloeschen("KI 2 ")
        elif Spieler_Gelb_2_0 == True:
            labelloeschen("Mensch  ")
            labelloeschen("KI  ")
        elif Spieler_Gelb_1_0 == False and Spieler_Gelb_2_0 == False: 
            labelloeschen("KI  ")
            labelloeschen("KI 2 ")
        if Spieler_Gruen_1_0 == True:
            labelloeschen("Mensch")
            labelloeschen("KI 2")
        elif Spieler_Gruen_2_0 == True:
            labelloeschen("Mensch")
            labelloeschen("KI")
        elif Spieler_Gruen_1_0 == False and Spieler_Gruen_2_0 == False:
            labelloeschen("KI")
            labelloeschen("KI 2")
        if Spieler_Gelb_1_0 != None and Spieler_Gruen_1_0 != None :
            Spielbeginnt = True
            #================================
            if Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_1_0 == True and Spieler_Gruen_1_0 == False and Spieler_Gruen_2_0 == False:
                KI_Gelb_1_0.setSpielfeld(Array)
                Vier_Gewinnt.setSpielzug(KI_Gelb_1_0.Spielzuggenerieren())
                Vier_Gewinnt.ausführen()
            #=====================
            #==========================
            if Vier_Gewinnt.getRestSpielzüge() %2 == 1 and Vier_Gewinnt.getSpielbeendet() ==False and Spieler_Gelb_2_0 == True and Spieler_Gruen_1_0 == False and Spieler_Gruen_2_0 == False:
                KI_Gelb_2_0.setSpielfeld(Array)
                Vier_Gewinnt.setSpielzug(KI_Gelb_2_0.Spielzuggenerieren())
                Vier_Gewinnt.ausführen()
            #=================================

            __Spielfeldgenerieren()



    # wenn Spielbeendet ist und ein neues Match starten soll
    if Vier_Gewinnt.getSpielbeendet() == True:
        g = False
        # Neues Match
        if xmouse >= 18 and xmouse <= 135 and ymouse >=540 and ymouse <=555:
            Vier_Gewinnt.neuesMatch()
            __Spielfeldgenerieren()
            g = True
        # Neues Spiel
        if xmouse >= 148 and xmouse <= 248 and ymouse >=538 and ymouse <=555:
            Vier_Gewinnt = viergewinntklasse([["w" for x in range(7)] for y in range(6)])
            Spieler_Gelb_1_0 = None
            Spieler_Gelb_2_0 = None
            Spieler_Gruen_1_0 = None
            Spieler_Gruen_2_0 = None
            Spielbeginnt = False
            LabelListe.clear()
            labelsetzen("Spielstand",400,450)
            labelsetzen("Spieler Gelb :",400,500)
            labelsetzen("Spieler Grün :",400,550)
            Spielbeginnt = False
            # Labels zur Auswahl der Spieler
            labelsetzen("Spieler 1",550 ,50)
            labelsetzen("Spieler 2",550, 200)
            # Spieler 1
            labelsetzen("Mensch  ",500,100)
            labelsetzen("KI  ",600,100)
            labelsetzen("KI 2 ",650,100)
        
            # Spieler 2
            labelsetzen("Mensch",500,250)
            labelsetzen("KI",600,250)
            labelsetzen("KI 2",650,250)

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
            if len(LabelListe) > 11:
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
KI_Gruen_1_0 = KI("gr","ge")
KI_Gelb_1_0 = KI("ge","gr")

KI_Gruen_2_0 = VierGewinnt_KI_2("gr","ge")
KI_Gelb_2_0 = VierGewinnt_KI_2("ge","gr")
HEIGHT = 600
WIDTH = 700
sys.setrecursionlimit(10000)
Spieler_Gelb_1_0 = None
Spieler_Gruen_1_0 = None

Spieler_Gelb_2_0 = None
Spieler_Gruen_2_0 = None

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
Spielbeginnt = False
# Labels zur Auswahl der Spieler
labelsetzen("Spieler 1",550 ,50)
labelsetzen("Spieler 2",550, 200)
# Spieler 1
labelsetzen("Mensch  ",500,100)
labelsetzen("KI  ",600,100)
labelsetzen("KI 2 ",650,100)
        
# Spieler 2
labelsetzen("Mensch",500,250)
labelsetzen("KI",600,250)
labelsetzen("KI 2",650,250)


pgzrun.go()

