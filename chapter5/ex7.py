#####################
#   Aufgabe 7, 5.8  #
#   v1.0            #
#   baehll          #
#   26.04.2018      #
#####################

def output(hour, bact):
    print("Stunde " + str(hour), end="    ")
    print(str(bact) + " Bakterien")

def multiply():
    bact = 100

    for h in range(49):
        output(h, bact)
        bact *= 4

multiply()
