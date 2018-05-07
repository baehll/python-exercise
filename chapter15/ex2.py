#####################
#   Aufgabe 1,15.14 #
#   v2.0            #
#   baehll          #
#   07.05.2018      #
#####################
from tkinter import *

class Waehrungsrechner:

    def __init__(self):
        self.fenster = Tk()
        self.kurs = IntVar()
        self.intro = Label(master=self.fenster, text="Geben sie einen Beitrag in EUR ein\nund wählen sie eine Währung", font=("Arial", 15))
        self.us = Radiobutton(master=self.fenster, text="US-Dollar", value=75, variable=self.kurs)
        self.gbp = Radiobutton(master=self.fenster, text="Britisches Pfund", value=125, variable=self.kurs)
        self.betrag = Entry(master=self.fenster)
        self.berechnen = Button(master=self.fenster, text="Rechnung", command=self.umwandeln)
        self.output = Label(master=self.fenster, text="Einen Betrag eingeben und umwandeln druecken")
        
        self.intro.pack()
        self.betrag.pack()
        self.us.pack()
        self.gbp.pack()
        self.berechnen.pack()
        self.output.pack()

        self.us.select()

        self.fenster.mainloop()

    def umwandeln(self):
        x = int(self.betrag.get()) * int(self.kurs.get()) / 100
        
        if (self.kurs.get() < 100):
            x = str(x) + " USD"
        else:
            x = str(x) + " GBP"

        self.output.config(text=x)

w = Waehrungsrechner()