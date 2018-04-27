#####################
#   Aufgabe 5, 7.7  #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

damen = {"D1", "D2", "D3", "D4"}
herren = {"H1", "H2", "H3", "H4"}
tanzlehrer = {"T1"}

paare = set(frozenset((a, b))
            for a in damen | tanzlehrer
            for b in herren | tanzlehrer
            if a != b)

for p in paare:
    print(tuple(p), end=" ")
