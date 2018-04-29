#####################
#   Aufgabe 1, 9.7  #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

import time

try:
    datei = open("./marathon.txt", "w")
except:
    print("Datei nicht geöffnet")    

while True:
    startNr = input("Startnummer: ")
    if(startNr == ""):
        break
    
    zeit = str(time.asctime())
    print("Startnummer: " + startNr, zeit, sep="\t", file=datei)

    datei.flush()

print("Die Daten befinden sich in ./marathon.txt")


