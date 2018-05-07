from tkinter import *
class Buchstabenregler:
    def __init__(self):
        self.fenster = Tk()
        self.label = Label(self.fenster, text="A", font=("Arial", 4))
        self.scale = Scale(self.fenster, length="3c", from_=4, to=60, command=self.setzeGroesse)
        self.label.pack(side=LEFT)
        self.scale.pack(side=RIGHT)
        self.fenster.mainloop()

    def setzeGroesse(self, event):
        x = int(self.scale.get())
        self.label.config(font=("Arial", x))

b = Buchstabenregler()