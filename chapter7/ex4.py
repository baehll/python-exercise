#####################
#   Aufgabe 4, 7.7  #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

#quersumme der seiten < 20
dreiecke = set(frozenset((a,b,c))
            for a in range(1, 20)
            for b in range(1, 20)
            for c in range(1, 20)
            if a**2+b**2 == c**2)

for d in dreiecke:
    print(tuple(d), end=" ")