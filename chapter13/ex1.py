#####################
#   Aufgabe 1, 13.7 #
#   v1.0            #
#   baehll          #
#   03.05.2018      #
#####################
from random import randint

class Staumelder:
    meldungen = [
        "Ein Stau von {laenge} Länge erwartet Sie auf der {autobahn} {richtung} am {stelle}.",
        "Auf der {autobahn} {richtung} am {stelle} {laenge} Stau."
    ]

    def __init__(self, t):
        self.__autobahn, self.__richtung, self.__stelle, self.__laenge = t

    def __run(self):
        text = self.meldungen[randint(0, len(self.meldungen) - 1)].format(laenge=self.__laenge, autobahn=self.__autobahn, richtung=self.__richtung, stelle=self.__stelle)
        return text

    def __str__(self):
        text = self.__run()
        return text

stau = Staumelder(("A1", "Richtung Köln", "Westhofener Kreuz", "6 km"))
print(stau)
        