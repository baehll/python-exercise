#####################
#   Aufgabe 3, 13.7 #
#   v1.0            #
#   baehll          #
#   04.05.2018      #
#####################

def woerter(text):
    text = text.lower()
    for p in ".,:-?!;":
        text.replace(p, "")
    liste = text.split()
    woerterbuch = []
    while liste:
        wort = liste[0]
        anzahl = 0
        while wort in liste:
            liste.remove(wort)
            anzahl += 1
        woerterbuch += [(wort, anzahl)]
        woerterbuch.sort()
    return woerterbuch





s = Suchmaschine("daten/dertext.txt")


