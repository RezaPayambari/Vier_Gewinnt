import unittest
from Vier_Gewinnt_Klasse import viergewinntklasse

class Test_test_VierGewinnt_Klasse(unittest.TestCase):
    # Überprüfung des Spielergebnisses
    #def test_A(self):
    #    viergewinnt = viergewinntklasse()
    #    Array = [["w" for x in range(7)] for y in range(6)]
    #    Array[5][0] = "gr"
    #    Array[5][1] = "gr"
    #    Array[5][5] = "gr"
    #    Array[4][3] = "gr"
    #    Array[3][3] = "gr"
    #    Array[1][3] = "gr"

    #    Array[5][2] = "ge"
    #    Array[5][3] = "ge"
    #    Array[5][4] = "ge"
    #    Array[4][1] = "ge"
    #    Array[4][2] = "ge"
    #    Array[2][3] = "ge"
    #    Array[3][2] = "ge"
    #    Array[3][1] = "ge"

    #    viergewinnt._viergewinntklasse__Array = Array
    #    viergewinnt._viergewinntklasse__Spielergebnis()
    #    Output = viergewinnt._viergewinntklasse__Ergebnis
    #    self.assertEqual("",Output,"Überprüfung ist nicht korrekt")


    def test_B(self):
        viergewinnt = viergewinntklasse()
        Array = [["w" for x in range(7)] for y in range(6)]
        Array[0][0] = 'ge'
        Array[1][0] = 'gr'
        Array[2][0] = 'ge'
        Array[3][0] = 'ge'
        Array[4][0] = 'gr'
        Array[5][0] = 'ge'
        Array[0][1] = 'gr'
        Array[1][1] = 'gr'
        Array[2][1] = 'ge'
        Array[3][1] = 'gr'
        Array[4][1] = 'ge'
        Array[5][1] = 'gr'
        Array[0][2] = 'ge'
        Array[1][2] = 'gr'
        Array[2][2] = 'ge'
        Array[3][2] = 'gr'
        Array[4][2] = 'ge'
        Array[5][2] = 'gr'
        Array[1][3] = 'ge'
        Array[2][3] = 'gr'
        Array[3][3] = 'ge'
        Array[4][3] = 'gr'
        Array[5][3] = 'ge'
        Array[0][4] = 'ge'
        Array[1][4] = 'ge'
        Array[2][4] = 'gr'
        Array[3][4] = 'ge'
        Array[4][4] = 'gr'
        Array[5][4] = 'ge'
        Array[0][5] = 'gr'
        Array[1][5] = 'gr'
        Array[2][5] = 'gr'
        Array[3][5] = 'ge'
        Array[4][5] = 'gr'
        Array[5][5] = 'ge'
        Array[0][6] = 'ge'
        Array[1][6] = 'gr'
        Array[2][6] = 'ge'
        Array[3][6] = 'gr'
        Array[4][6] = 'ge'
        Array[5][6] = 'gr'


        viergewinnt._viergewinntklasse__Array = Array
        viergewinnt._viergewinntklasse__Spielergebnis()
        Output = viergewinnt._viergewinntklasse__Ergebnis
        self.assertEqual("",Output,"Überprüfung ist nicht korrekt")

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Absturz")