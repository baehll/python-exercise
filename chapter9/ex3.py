#####################
#   Aufgabe 2, 9.7  #
#   v1.0            #
#   baehll          #
#   29.04.2018      #
#####################
import pickle

dictPath = "dict.dmp"
telefonBuch = {}

def inputDialog():
    print("(S)uche nach Telefonnummer")
    print("(N)eue Telefonnummer eintragen")
    print("(A)lle Telefonnummern ausgeben")
    print("(E)nde")

    choice = input("Ihre Wahl: ")
    print("")
    return choice

def openTel():
    tel = {}
    try:
        datei = open(dictPath, "rb")
        tel = pickle.load(datei)
        datei.close()
    except:
        print("Datei nicht gefunden")

    return tel

def neueNummer(telefonBuch):
    name = input("Name: ")
    num = int(input("Nummer: "))

    telefonBuch[name] = num

    print("Neuer Eintrag gespeichert")
    print("")
    print("")
    return telefonBuch

def sucheNummer(telefonBuch):
    name = input("Name: ")

    print("Nummer: ", telefonBuch[name])

    print("")
    print("")
    print("")

def alleNummern(telefonBuch):
    print("Name", "Nummer", sep="\t\t")
    print("------------------------------")

    for item in telefonBuch.keys():
        print(item, telefonBuch[item], sep="\t\t")

    print("")
    print("")
    print("")

def main():
    global telefonBuch
    global dictPath
    telefonBuch = openTel()
    choice = ""

    while choice not in ["e", "E"]:
        choice = inputDialog()
        if(choice in ["n", "N"]):
            telefonBuch = neueNummer(telefonBuch)
        elif(choice in ["a", "A"]):
            alleNummern(telefonBuch)
        elif(choice in ["s", "S"]):
            sucheNummer(telefonBuch)

    try:
        datei = open(dictPath, "wb")
        pickle.dump(telefonBuch, datei)
        datei.close()
    except:
        print("Fehler beim speichern")

    
    print("Danke und auf Wiedersehen")

main()