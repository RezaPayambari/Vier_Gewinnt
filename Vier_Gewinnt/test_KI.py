import unittest
from Vier_Gewinnt_KI import KI

class Test_test_KI(unittest.TestCase):
    ###################################################
    #                                                 #
    #  Gewinnen des Gegners soll verhindert werden    #
    #                                                 #
    ###################################################

    # erkennung von Diagonalen, wenn drei Steine gegeben sind
    #==========================================================================================================
    def test_A(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[2][1] = "ge"
        Array[3][2] = "ge"
        Array[4][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Diagonale nach rechts unten funktionier nicht")

    def test_A_1(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[1][2] = "gr"
        Array[2][3] = "gr"
        Array[3][0] = "gr"
        #Array[3][4] = "gr"
        Array[4][1] = "gr"
        Array[5][2] = "gr"
        #====
        Array[1][0] = "gr"
        Array[2][1] = "ge"
        Array[3][2] = "ge"
        Array[4][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Diagonale nach rechts unten funktionier nicht")
    #=========================================================================================================================================



    # Erkennung von Waagerechten wenn drei Steine gegeben sind
    #=========================================================================================================================================
    def test_B(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "ge"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(3,Output,"einfache waagerechte funktioniert nicht")

    def test_C(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"einfache waagerechte mit einem grünen Stein funktioniert nicht")

    def test_D(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"waagerechte funktioniert nicht")

    def test_E(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(6,Output,"waagerechte funktioniert nicht")
    #==============================================================================================================================

    # Erkennung von senkrechten wenn drei Steine gegeben sind
    #============================================================================================================================
    def test_F(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][5] = "gr"
        Array[4][3] = "gr"
        Array[3][3] = "gr"
        Array[1][3] = "gr"

        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[4][1] = "ge"
        Array[4][2] = "ge"
        Array[2][3] = "ge"
        Array[3][2] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"senkrechte funktioniert nicht")

    #==============================================================================================================================

    # Überprüfung ob KI spalten auslässt, damit sie nicht verliert
    #============================================================================================================================
    def test_G(self):
        for i in range(100):
            Viergewinnt_ki = KI("gr","ge")
            Array = [["w" for x in range(7)] for y in range(6)]
            Array[5][5] = "gr"
            Array[5][4] = "gr"
            Array[4][5] = "gr"
            Array[4][2] = "gr"
            Array[2][3] = "gr"


            Array[5][2] = "ge"
            Array[5][3] = "ge"
            Array[4][4] = "ge"
            Array[4][3] = "ge"
            Array[3][2] = "ge"
            Array[3][3] = "ge"
            Array[3][4] = "ge"

            Viergewinnt_ki.setSpielfeld(Array)
            Output = Viergewinnt_ki.Spielzuggenerieren()
            self.assertIsNot(5,Output,"waagerecht und Diagonal")
            #print("Zug: "+str(Output))
    
    def test_H(self):
        for i in range(100):
            Viergewinnt_ki = KI("gr","ge")
            Array = [["w" for x in range(7)] for y in range(6)]
            Array[4][2] = "ge"
            Array[4][3] = "ge"
            Array[4][4] = "ge"
            Array[5][2] = "gr"
            Array[5][3] = "ge"
            Array[5][4] = "gr"

            Viergewinnt_ki.setSpielfeld(Array)
            Output = Viergewinnt_ki.Spielzuggenerieren()
            self.assertIsNot(1,Output,"waagerechte")
            self.assertIsNot(5,Output,"waagerechte")
            #print("Zug: "+str(Output))

    # zwei Stein Erkennung
    def test_I(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][4] = "ge"
        Array[5][3] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test I ist fehlgeschlagen")

    def test_J(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][3] = "ge"
        Array[4][3] = "gr"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test J ist fehlgeschlagen")

    def test_K(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][3] = "ge"
        Array[4][3] = "ge"

        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(3,Output,"Test K ist fehlgeschlagen")

    def test_L(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "gr"

        Array[4][0] = "gr"
        Array[4][1] = "ge"
        Array[4][2] = "gr"
        Array[4][3] = "gr"
        Array[4][4] = "gr"
        
        Array[3][0] = "ge"
        Array[3][1] = "ge"
        Array[3][2] = "ge"
        Array[3][3] = "gr"

        Array[2][1] = "gr"
        Array[2][2] = "gr"
        Array[2][3] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(1,Output,"Test L ist fehlgeschlagen")

    def test_M(self):

        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[5][0] = "gr"
        Array[5][1] = "ge"
        Array[5][2] = "ge"
        Array[5][3] = "ge"
        Array[5][4] = "gr"

        Array[4][0] = "gr"
        Array[4][1] = "ge"
        Array[4][2] = "gr"
        Array[4][3] = "gr"
        Array[4][4] = "gr"
        
        Array[3][0] = "ge"
        Array[3][1] = "ge"
        Array[3][2] = "ge"
        Array[3][3] = "gr"

        Array[2][1] = "gr"
        Array[2][2] = "gr"
        Array[2][3] = "ge"

        Array[1][1] = "ge"
    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(4,Output,"Test M ist fehlgeschlagen")

    def test_N(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]


        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"

        Array[4][3] = "gr"
        Array[4][4] = "gr"

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test N ist fehlgeschlagen")

    def test_O(self):
        Viergewinnt_ki = KI("ge","gr")
        Array = [["w" for x in range(7)] for y in range(6)]

        Array[5][0] = "gr"
        Array[5][1] = "gr"
        Array[5][2] = "gr"
        Array[5][3] = "ge"
        Array[5][4] = "ge"
        Array[5][5] = "ge"
        Array[5][6] = "gr"

        Array[4][3] = "gr"
        Array[4][4] = "gr"

    
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(2,Output,"Test N ist fehlgeschlagen")




        


if __name__ == '__main__':
    unittest.main()
