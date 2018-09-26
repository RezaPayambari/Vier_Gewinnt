import pgzrun
from Vier_Gewinnt_Klasse import viergewinntklasse

Vier_Gewinnt = viergewinntklasse()
HEIGHT = 4000
WIDTH = 5000


xposition = 30
yposition = 30
Spielerliste = []
Array = [["w" for x in range(7)] for y in range(6)]
for x in range(7):
    yposition = -30
    xposition = xposition +5
    for y in range(6):
        yposition = yposition +65
        Spieler = Actor("spieler_weiß")
        Spieler.x = xposition
        Spieler.y = yposition
        Spielerliste.append(Spieler)
    xposition = xposition + 60

def draw():
    screen.fill("green")
    for Spieler in Spielerliste:
        Spieler.draw()
    

def on_mouse_down(pos):
    xmouse = pos[0]
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
    if spalte != 100:
        Vier_Gewinnt.setSpielzug(spalte)
        Vier_Gewinnt.ausführen()
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
        screen.draw.text("hello world", (3000, 100))
        draw()


    
pgzrun.go()

