#####################
#   Aufgabe 2, 6.15 #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################
import random

def verstecke(s, n=1):
    s = s.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputString = ""
    print("Vorher: " + s)
    for i in range(len(s)):
        outputString += s[i]
        for j in range(n):
            outputString += alphabet[random.randint(0, len(alphabet) - 1)]
    print("Nachher: " + outputString)


verstecke("hallo", 4)
