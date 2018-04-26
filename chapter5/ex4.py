#####################
#   Aufgabe 4, 5.8  #
#   v1.0            #
#   baehll          #
#   26.04.2018      #
#####################

def schaltjahrChecker():
    jahr = int(input("Bitte ein Jahr eingeben: "))

    if ((jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0)):
        print(str(jahr) + " ist ein Schaltjahr")
    else:
        print(str(jahr) + " ist kein Schaltjahr")


schaltjahrChecker()