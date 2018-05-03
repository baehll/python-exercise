#####################
#   Aufgabe 1,12.4.3#
#   v1.0            #
#   baehll          #
#   02.05.2018      #
#####################

import pickle
from musical import *

class Manager:
    __menuetext = """
    Musical-Manager
    ------------------
    (n)eue Vorstellung
    (U)eberblick Vorstellungen
    (S)torniere Vorstellung
    (E)nde
    """

    def __init__(self, datei):
        self.__datei = datei
        self.__lade_musical()
        self.__run()
    
    def __run(self):
        print(self.__menuetext)
        wahl = "-"
        while wahl not in ["e", "E"]:
            wahl = input("Auswahl: ")
            if wahl in ["n", "N"]:
                self.__neueVorstellung()
            elif wahl in ["u", "U"]:
                print(self.__musical)
            elif wahl in ["s", "S"]:
                self.__storniere()
            print(self.__menuetext)
        print("Danke für die Benutzung vom Musical-Manager")
        self.__speichern()

    def __storniere(self):
        datum = input("Datum der Vorstellung: ")
        text = self.__musical.storniere(datum)
        print(text)

    def __neueVorstellung(self):
        datum = input("Termin: ")
        beginn = input("Beginn der Vorstellung: ")
        vorstellung = Vorstellung(datum, beginn, self.__musical.saal)
        self.__musical.neueVorstellung(vorstellung)

    def __neuesMusical(self):
        titel = input("Titel: ")
        eintrittspreis = float(input("Eintrittspreis: "))
        anzahl_reihen = int(input("Anzahl Sitzreihen: "))
        liste = []
        for i in range(anzahl_reihen):
            sitze = int(input("Sitze in Reihe " + str(i + 1) + ": "))
            liste.append(sitze)
        saal = Saal(liste)
        self.__musical = Musical(titel, eintrittspreis, saal)
    
    def __lade_musical(self):
        try:
            f = open(self.__datei, "rb")
            self.__musical = pickle.load(f)
            f.close()
            print("\n            W I L L K O M M E N")
            print("beim Manangement-System für das Musical", self.__musical.titel)
        except:
            print("Kein Musical gespeichert")
            print("Richten Sie ein neues Musical ein.")
            self.__neuesMusical()
    
    def __speichern(self):
        f = open(self.__datei, "wb")
        pickle.dump(self.__musical, f)
        f.close()

m = Manager("daten/hairspray.txt")