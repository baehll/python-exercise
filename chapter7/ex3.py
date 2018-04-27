#####################
#   Aufgabe 3, 7.7  #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

import random

farben = ["Kreuz", "Karo", "Pik", "Herz"]
werte = [7, 8, 9, 10, "B", "D", "K", "A"]

spiel = [(f, w) for f in farben for w in werte]

for i in range(len(spiel) - 1):
    position = random.randint(0, len(spiel) -1)
    spiel[i], spiel[position] = spiel[position], spiel[i]

print(spiel)