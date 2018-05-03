#####################
#   Aufgabe 1,12.4.3#
#   v1.0            #
#   baehll          #
#   02.05.2018      #
#####################

import pickle

class Musical:
    def __init__(self, titel, eintrittspreis, saal):
        self.titel = titel
        self.eintrittspreis = eintrittspreis
        self.saal = saal
        self.vorstellungen = []

    def getVorstellungen(self, datum):
        for vorstellung in self.vorstellungen:
            if vorstellung.datum == datum: return vorstellung
    
    def neueVorstellung(self, vorstellung):
        self.vorstellungen += [vorstellung]

    def storniere(self, datum):
        vorstellung = self.getVorstellungen(datum)
        if not vorstellung:
            return "Keine Vorstellung am Tag"
        else:
            zuschauerliste = vorstellung.getZuschauer()
            text = "Liste aller Vorstellungen an diesem Tag"
            text += datum + "\n\n"
            for z in zuschauerliste:
                text += z.name + " " + z.tel + "\n"
            self.vorstellungen.remove(vorstellung)
            return text

    def __str__(self):
        beschreibung = "\n" + self.titel + "\n" + len(self.titel)*"=" + "\n"
        for vorstellung in self.vorstellungen:
            beschreibung += str(vorstellung) + "\n"
        return beschreibung

class Vorstellung:
    def __init__(self, datum, beginn, saal):
        self.datum = datum
        self.beginn = beginn
        self.saalbelegung = Saalbelegung(saal)
        self.saal = saal

    def getZuschauer(self):
        zuschauerListe = []
        for reihe in self.saalbelegung:
            for platz in reihe:
                if (platz.zuschauer):
                    zuschauerListe += [platz.zuschauer]
        return zuschauerListe
    
    def __str__(self):
        beschreibung = self.datum + "\n" + str(self.saalbelegung.getFreiePlaetze()) + " freie Plätze\n"
        return beschreibung

class Saalbelegung:
    def __init__(self, saal):
        self.belegung = []
        self.saal = saal
        for i in range(len(saal.plaetzeProReihe)):
            reihe = []
            for j in range(saal.plaetzeProReihe[i]):
                platz = Platz()
                reihe += [platz]
            self.belegung += [reihe]
    
    def buche(self, reihe, platz, zuschauer):
        if not self.belegung[reihe][platz].belegt():
            self.belegung[reihe][platz].belege(zuschauer)
            return "Platz gebucht"
        else: return "Platz schon belegt"
    
    def getFreiePlaetze(self):
        frei = 0
        for reihe in self.belegung:
            for platz in reihe:
                if not platz.belegt(): frei += 1
        return frei

    def __str__(self):
        beschreibung = "Saalbelegung\n"
        beschreibung += "\tPlatz: 1  2  3  4  5  6  7  8  9  10 11 12 13 14\n"
        nr = 1
        for reihe in self.belegung:
            beschreibung += "Reihe " + format(nr, "2d") + ": "
            for platz in reihe:
                beschreibung += str(platz)
            nr += 1
            beschreibung += "\n"
        return beschreibung

class Zuschauer:
    def __init__(self, name, tel):
        self.name, self.tel = name, tel

class Platz:
    def __init__(self):
        self.zuschauer = None

    def belegt(self):
        if self.zuschauer: return True
        else: return False 
    
    def belege(self, zuschauer):
        self.zuschauer = zuschauer

    def __str__(self):
        if self.belegt():
            return self.zuschauer.name[:2] + " "
        else: return "-- "

class Saal:
    def __init__(self, liste):
        self.plaetzeProReihe = liste
