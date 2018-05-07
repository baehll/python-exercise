#####################
#   Aufgabe 2, 14.4 #
#   v1.0            #
#   baehll          #
#   07.05.2018      #
#   fehlerhaft      #
#####################
import os

suchwort = input("Suchwort: ")
vz = input("Wurzelverzeichnis: ")

gelesen = 0
fehlerhaftGelesen = 0
ergebnisse = {}

os.chdir(vz)

dateien = os.listdir(vz)
for d in dateien:
    wrkDir = os.path.join(vz, d)
    if(os.path.isfile(wrkDir)):
        try:
            f = open(wrkDir, "r")
            lines = f.read()
            vorkommnisse = lines.count(suchwort)
            if (vorkommnisse > 0):
                ergebnisse[wrkDir] = vorkommnisse
            f.close()
        except:
            fehlerhaftGelesen += 1
    gelesen += 1

for e in ergebnisse:
    e.key

print("Es wurden " + str(gelesen) + " Dateien gelesen.")
print(str(fehlerhaftGelesen) + " Dateien waren nicht lesbar.")


