#####################
#   Aufgabe 1, 14.4 #
#   v1.0            #
#   baehll          #
#   07.05.2018      #
#####################
from os import mkdir


vName = input("Vorname: ")
nName = input("Nachname: ")

vzName = vName[:6] + nName[:3]

mkdir("./chapter14/python/projekte/user/" + vzName.lower())

print("Verzeichnis angelegt")