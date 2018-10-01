import tkinter
from Vier_Gewinnt_Klasse import viergewinntklasse

class GUI:
    def __init__(self, title="Blank Window"):
        self.root = tkinter.Tk() 
        self.root.title(title) 
        # Spieler figuren 
        self.spielergruen = tkinter.PhotoImage (file="Spieler_Gruen.gif") 
        self.spielergelb = tkinter.PhotoImage (file="Spieler_Gelb.gif") 
        self.Spielerweiß = tkinter.PhotoImage (file="Spieler_Weiß.gif") 
        self.Oberfläche_erzeugen() 
        self.__viergewinnt = viergewinntklasse() 
        self.__Array = [["w" for x in range(7)] for y in range(6)] 


    
        
    def Oberfläche_erzeugen(self):
        #### Spielfeld
        
         # Buttons hinzufügen
        self.btn1 = tkinter.Button(self.root, text="Einwerfen", command=self.btn1_Click)
        self.btn2 = tkinter.Button(self.root, text="Einwerfen", command=self.btn2_Click)
        self.btn3 = tkinter.Button(self.root, text="Einwerfen", command=self.btn3_Click)
        self.btn4 = tkinter.Button(self.root, text="Einwerfen", command=self.btn4_Click)
        self.btn5 = tkinter.Button(self.root, text="Einwerfen", command=self.btn5_Click)
        self.btn6 = tkinter.Button(self.root, text="Einwerfen", command=self.btn6_Click)
        self.btn7 = tkinter.Button(self.root, text="Einwerfen", command=self.btn7_Click)
        # Position der Buttons fixieren
        self.btn1.grid(row=1, column=1)
        self.btn2.grid(row=1, column=2)
        self.btn3.grid(row=1, column=3)
        self.btn4.grid(row=1, column=4)
        self.btn5.grid(row=1, column=5)
        self.btn6.grid(row=1, column=6)
        self.btn7.grid(row=1, column=7)
        for i in range(1,8):
            for ii in range(2,8):
                Spielfeld = tkinter.Label(self.root, image=self.Spielerweiß, borderwidth=3, relief="solid")
                Spielfeld.grid(column=i, row=ii)
        label = tkinter.Label(text="")
        label.grid(column=3, columnspan=4, row=8)

        #  Erweiterung
        self.btn8 = tkinter.Button(self.root, text="Spieler Grün", command=self.btn8_Click)
        self.btn9 = tkinter.Button(self.root, text="KI", command=self.btn9_Click)
        self.btn10 = tkinter.Button(self.root, text="Spieler Gelb", command=self.btn10_Click)
        self.btn11 = tkinter.Button(self.root, text="KI", command=self.btn11_Click)
        self.btn12 = tkinter.Button(self.root, text="Neues Spiel", command=self.btn12_Click)
        self.btn13 = tkinter.Button(self.root, text="Neues Match", command=self.btn13_Click)

        # Position der Buttons fixieren
        self.btn8.grid(row=2, column=9)
        self.btn9.grid(row=2, column=11)
        self.btn10.grid(row=3, column=9)
        self.btn11.grid(row=3, column=11)
        self.btn12.grid(row=8, column=9)
        self.btn13.grid(row=8, column=11)


        Label = tkinter.Label(text="Spieler Grün:")
        Label.grid(column=9, row=5)
        Label = tkinter.Label(text="0")
        Label.grid(column=11, row=5)
        Label = tkinter.Label(text="Spieler Gelb:")
        Label.grid(column=9, row=6)
        Label = tkinter.Label(text="0")
        Label.grid(column=11, row=6)


        
    def zugausführen(self,Spalte):  
        self.__viergewinnt.setSpielzug(Spalte)
        self.__viergewinnt.ausführen()
        self.__Array = self.__viergewinnt.getArray()
        self.überprüfung()

        for i in range(1,8):
            for ii in range(2,8):
                if self.__Array[ii-2][i-1] == "w":
                    Spielfeld = tkinter.Label(self.root, image=self.Spielerweiß, borderwidth=3, relief="solid")
                elif self.__Array[ii-2][i-1] == "gr":
                    Spielfeld = tkinter.Label(self.root, image=self.spielergruen, borderwidth=3, relief="solid")
                elif self.__Array[ii-2][i-1] == "ge":
                    Spielfeld = tkinter.Label(self.root, image=self.spielergelb, borderwidth=3, relief="solid")
                Spielfeld.grid(column=i, row=ii)



    def überprüfung(self):
        if self.__viergewinnt.getErgebnis() == "ge":
            label = tkinter.Label(text="Spieler Gelb hat gewonnen!!!")
            label.grid(column=3, columnspan=4, row=8)
        elif self.__viergewinnt.getErgebnis() == "gr":
            label = tkinter.Label(text="Spieler Grün hat gewonnen!!!")
            label.grid(column=3, columnspan=4, row=8)
        elif self.__viergewinnt.getErgebnis() == "un":
            label = tkinter.Label(text="Unentschieden!!!")
            label.grid(column=3, columnspan=4, row=8)

    def btn1_Click(self):
        self.zugausführen(0)

    def btn2_Click(self):
        self.zugausführen(1)

    def btn3_Click(self):
        self.zugausführen(2)

    def btn4_Click(self):
        self.zugausführen(3)

    def btn5_Click(self):
        self.zugausführen(4)

    def btn6_Click(self):
        self.zugausführen(5)

    def btn7_Click(self):
        self.zugausführen(6)

    def btn8_Click(self):
        print("")

    def btn9_Click(self):
        print("")

    def btn10_Click(self):
        print()

    def btn11_Click(self):
        print()

    def btn12_Click(self):
        self.root.destroy()
        w = GUI()
        w.run()

    def btn13_Click(self):
        print()


        
    def run(self):
        self.root.mainloop()
        


w = GUI()
w.run()

