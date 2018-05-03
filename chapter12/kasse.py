#####################
#   Aufgabe 1,12.4.3#
#   v1.0            #
#   baehll          #
#   02.05.2018      #
#####################

import pickle
from musical import *

class Kartenverkauf: 
    __menuetext = """
    Muscial-Ticketservice
    ---------------------
    (B)uchung
    (U)eberblick Vorstellungen
    (E)nde
    """

    def __init__(self, datei):
        self.__datei = datei
        self.__lade_musical()
        self.__run()

    def __lade_musical(self):
        try:
            f = open(self.__datei, "rb")
            self.__musical = pickle.load(f)
            f.close()
            print("\n           W I L L K O M M E N")
            print("beim Buchungssystem für das Musical", self.__musical.titel)
        except:
            print("Kein Musical gespeichert")
    
    def __run(self):
        print(self.__menuetext)
        wahl = "-"
        while wahl not in "eE":
            wahl = input("Auswahl: ")
            if wahl in "bB": 
                self.__buchen()
            elif wahl in "uU": 
                print(self.__musical)
            print(self.__menuetext)
        print("Danke für die Benutzung von Musical-Ticketservice")
        self.__speichern()
    
    def __auskunft(self, datum, zuschauer):
        """
            Name:
            Eintrittspreis:

            Titel:
            Datum der Vorstellung:
            Beginn der Vorstellung:
            Reihe/Platznummer:
        """

        vorstellung = self.__musical.getVorstellungen(datum)
        print("Musicaltitel: \t\t", self.__musical.titel)
        print("Datum der Vorstellung: \t", vorstellung.datum)
        print("Uhrzeit: \t\t", vorstellung.beginn)
        print("Eintrittspreis: \t\t", self.__musical.eintrittspreis)
        print("Reihe".center(10), "Platz".center(10), sep="|")
        print("--------------------")
        for reihe in range(len(vorstellung.saalbelegung.belegung)):
            for platz in range(len(vorstellung.saalbelegung.belegung[reihe])):
                if vorstellung.saalbelegung.belegung[reihe][platz].zuschauer == zuschauer:
                    print("{reihe}".format(reihe=reihe+1).center(10),"{platz}".format(platz=platz+1).center(10), sep="|")
        

    def __buchen(self):
        datum = input("Datum der Vorstellung: ")
        vorstellung = self.__musical.getVorstellungen(datum)
        if not vorstellung:
            print("An diesem Tag gibt es keine Vorstellung")
        else:
            print(vorstellung.saalbelegung)
            name = input("Name: ")
            tel = input("Telefonnummer: ")
            zuschauer = Zuschauer(name, tel)
            reihe = "x"
            while reihe != "":
                reihe = input("Reihe: ")
                if reihe != "":
                    platz = input("Platz: ")
                    print(vorstellung.saalbelegung.buche(int(reihe) - 1, int(platz) - 1, zuschauer))
        self.__auskunft(datum, zuschauer)
    
    def __speichern(self):
        f = open(self.__datei, "wb")
        pickle.dump(self.__musical, f)
        f.close()

kasse = Kartenverkauf("daten/hairspray.txt")