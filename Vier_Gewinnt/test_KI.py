import unittest
from Vier_Gewinnt_KI import KI

class Test_test_KI(unittest.TestCase):
    def test_A(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[2][1] = "ge"
        Array[3][2] = "ge"
        Array[4][3] = "ge"
        Viergewinnt_ki.setSpielfeld(Array)
        Output = Viergewinnt_ki.Spielzuggenerieren()
        self.assertEqual(0,Output,"Diagonale nach rechts unten funktionier nicht")

    def test_A_1(self):
        Viergewinnt_ki = KI("gr","ge")
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[1][2] = "gr"
        Array[2][3] = "gr"
        Array[3][0] = "gr"
        Array[3][4] = "gr"
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
        self.assertEqual(2,Output,"waagerechte funktioniert nicht")




        


if __name__ == '__main__':
    unittest.main()
