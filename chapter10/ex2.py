#####################
#   Aufgabe 2, 10.11#
#   v1.0            #
#   baehll          #
#   30.04.2018      #
#####################

from ex1 import Ding

class Quader(Ding):
    def __init__(self, s, l, b, h):
        self.__laenge = l
        self.__breite = b
        self.__hoehe = h
        Ding.__init__(self, s, l*b*h)

    def __str__(self):
        return "Der Quader hat die Maße (l, b, h in cm): " + str(self.__laenge) + ", " + str(self.__breite) + ", " + str(self.__hoehe)

    def __gt__(self, q2):
        return self.getMasse() > q2.getMasse()
    
    def __ge__(self, q2):
        return self.getMasse() >= q2.getMasse()
    
    def __eq__(self, q2):
        return self.getMasse() == q2.getMasse()
    
silberbarren = Quader("Au", 2, 3, 4)
eisenbarren = Quader("Fe", 2, 3, 4)

print("Ist der Eisenbarren schwerer? ",  eisenbarren > silberbarren)
print("Ist der Goldbarren schwerer oder gleich schwer? ", eisenbarren >= silberbarren)
print("Sind die Barren gleich schwer? ", silberbarren == eisenbarren)