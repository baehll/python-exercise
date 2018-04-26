#####################
#   Aufgabe 10, 5.8 #
#   v1.0            #
#   baehll          #
#   26.04.2018      #
#####################

def defineDNA():
    dnaBasen = ["AT", "TA", "GC", "CG"]

    for a in dnaBasen:
        for b in dnaBasen:
            for c in dnaBasen:
                for d in dnaBasen:
                    print(a, b, c, d)

defineDNA()
