#####################
#   Aufgabe 4, 10.11#
#   v1.0            #
#   baehll          #
#   30.04.2018      #
#####################

class Laenge(object):
    __meter = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9143,
        "mil": 1609
    }

    def __init__(self, betrag, einheit):
        self.betrag = float(betrag)
        self.einheit = einheit
    
    def getMeter(self):
        return self.betrag * self.__meter[self.einheit]

    def __add__(self, l):
        s = self.getMeter() + l.getMeter()
        return Laenge(s/self.__meter[self.einheit], self.einheit)

    def __gt__(self, l):
        return self.getMeter() > l.getMeter()

    def __ge__(self, l):
        return self.getMeter() >= l.getMeter()
    
    def __eq__(self, l):
        return self.getMeter() == l.getMeter()

    def __str__(self):
        return str(self.betrag) + " " + self.einheit

penismann = Laenge(1.5, "m")
schuh = Laenge(30, "cm")

print("Erddurchmesser + Schuh", penismann + schuh)