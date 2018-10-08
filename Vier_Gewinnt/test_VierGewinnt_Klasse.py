import unittest
from Vier_Gewinnt_Klasse import viergewinntklasse

class Test_test_VierGewinnt_Klasse(unittest.TestCase):
    def test_A(self):
        viergewinnt = viergewinntklasse()
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
        Array[3][1] = "ge"

        viergewinnt._viergewinntklasse__Array = Array
        viergewinnt._viergewinntklasse__Spielergebnis()
        Output = viergewinnt._viergewinntklasse__Ergebnis
        self.assertEqual("",Output,"Überprüfung ist nicht korrekt")

if __name__ == '__main__':
    unittest.main()
