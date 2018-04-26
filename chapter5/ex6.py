#####################
#   Aufgabe 6, 5.8  #
#   v1.0            #
#   baehll          #
#   26.04.2018      #
#####################

def eingabe():
    print("Kreditrechner")
    summe = int(input("Kreditsumme in Euro: "))
    zinssatz = int(input("Zinssatz (Prozent pro Jahr): "))
    beitrag = int(input("Jährliche Rückzahlung in Euro: "))
    
    kreditRechner(summe, zinssatz, beitrag) 

def kreditRechner(summe, zinssatz, beitrag):
    jahr = 2018
    while True:
        zinsen = round(summe / 100 * zinssatz)
        tilgung = round(beitrag - zinsen)

        if(summe - tilgung < 0):
            print("Restforderung: " + str(summe) + " EUR")
            break
        else:
            summe = round(summe - tilgung)
            ausgabe(jahr, zinsen, tilgung, summe)
            jahr += 1

def ausgabe(jahr, zinsen, tilgung, summe):  
    print(str(jahr), end="    ")
    print("Zinsen: " + str(zinsen) + " EUR", end="    ")
    print("Tilgung: " + str(tilgung) + " EUR", end="    ")
    print("Restschulden: " + str(summe), end="\n")

eingabe()