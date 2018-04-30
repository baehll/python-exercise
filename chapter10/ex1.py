#####################
#   Aufgabe 1, 10.11#
#   v1.0            #
#   baehll          #
#   30.04.2018      #
#####################

class Ding(object):
    dichte = {
            "Fe":("Eisen", 7.87),
            "Au":("Gold", 19.32),
            "Ag":("Silber", 10.5)
        }
    def __init__(self, s, v):
        self.__volumen = v
        self._symbol = s

    def getMasse(self):
        return str(format(self._dichte[self._symbol][1] * self.__volumen, ".2f") + " g"
    
    def getVolumen(self):
        return str(format(self.__volumen, ".2f")) + " ccm"

    def __str__(self):
        return "Das Ding besteht aus " + str(self._dichte[self._symbol][0]) + \
        " (Symbol: " + self._symbol + ")" + \
        ", besitzt ein Volumen von " + self.getVolumen() + \
        " und wiegt " + self.getMasse()