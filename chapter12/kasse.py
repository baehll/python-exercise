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
            if wahl in "bB": self.__buchen()
            elif wahl in "uU": print(self.__musical)
            print(self.__menuetext)
        print("Danke für die Benutzung von Musical-Ticketservice")
        self.__speichern()
    
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
    
    def __speichern(self):
        f = open(self.__datei, "wb")
        pickle.dump(self.__musical, f)
        f.close()

kasse = Kartenverkauf("daten/hairspray.txt")