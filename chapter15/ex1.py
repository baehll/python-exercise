#####################
#   Aufgabe 1,15.14 #
#   v1.0            #
#   baehll          #
#   07.05.2018      #
#####################

from tkinter import * 

class Lichtschalter:
    def __init__(self):
        self.fenster = Tk()
        self.an = True
        self.schalter = StringVar()
        self.schalter.set("Licht an")
        self.label = Label(master=self.fenster, textvariable=self.schalter, bg="black", fg="white", width=20, height=5)
        self.switch = Button(master=self.fenster, text="I/O", command=self.wechseln)
        self.label.pack()
        self.switch.pack()
        self.fenster.mainloop()

    def wechseln(self):
        if (self.an):
            self.label.config(bg="white", fg="black")
            self.schalter.set("Licht an")
            self.an = not self.an
        else:
            self.label.config(bg="black", fg="white")
            self.schalter.set("Licht aus")
            self.an = not self.an

l = Lichtschalter()