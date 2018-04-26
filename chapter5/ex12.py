#####################
#   Aufgabe 12, 5.8 #
#   v1.0            #
#   baehll          #
#   26.04.2018      #
#####################
import time
import random

def output(correct):
    if(correct):
        print("Richtig!")
    else:
        print("Falsch, bitte nochmal probieren")

def trainer():
    start = time.time()

    for x in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        while True:
            erg = int(input(str(a) + "*" + str(b) + "="))
            if (erg == a * b):
                output(True)
                break
            else:
                output(False)
    
    zeit = time.time() - start

    print("Du hast " + str(round(zeit)) + "s gebraucht")

trainer()


