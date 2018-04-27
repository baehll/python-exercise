#####################
#   Aufgabe 4, 6.15 #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

def bewege(n, von, nach, ueber):

    if(n==1):
        print("Lege eine Scheibe von " + str(von) + " nach " + str(nach) + ".")
    else:
        bewege(n-1, von, ueber, nach)
        bewege(1, von, nach, ueber)
        bewege(n-1, ueber, nach, von)



bewege(5, 1, 3, 4)