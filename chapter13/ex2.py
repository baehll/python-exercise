#####################
#   Aufgabe 2, 13.7 #
#   v1.0            #
#   baehll          #
#   04.05.2018      #
#####################

class Pinnwand:

    def __init__(self):
        self.__zettel = []
    
    def hefteAn(self, notiz):
        #Analyse des Textes
        prio = notiz.count("!")
        self.__zettel.append((prio, notiz))

    def entferne(self):
        hoechste = 0
        zettel = 0
        for i in range(len(self.__zettel)):
            if self.__zettel[i][0] > hoechste:
                hoechste = self.__zettel[i][0]
                zettel = i
        print(self.__zettel[zettel][1])
        del self.__zettel[zettel]
    
    def __str__(self):
        ausgabe = "Notizen\n"
        zettelListe = self.__zettel[:]
        zettelListe.sort(reverse=True)
        print("Zettelliste: ")
        print(zettelListe)
        for z in zettelListe:
            ausgabe += z[1] + "\t"
            ausgabe += "(Priorität: " + str(z[0]) + ")" + "\n"
        return ausgabe

menue = """
    (N)eue Notiz anheften           (A)lle Notizen auflisten
    (W)ichtigste Notiz entfernen    (E)nde
"""

p = Pinnwand()

while True:
    print(menue)
    eingabe = input("Ihre Wahl: ")
    if eingabe in "nN":
        notiz = input("Notiz: ")
        while notiz != "":
            p.hefteAn(notiz)
            notiz = input("Notiz: ")
    elif eingabe in "aA":
        print(p)
    elif eingabe in "wW":
        p.entferne()
    elif eingabe in "eE":
        print("Tschüß!")
        break