from tkinter import *

class Farbmischer:
    def __init__(self):
        self.fenster = Tk()
        self.rot, self.gruen, self.blau = IntVar(), IntVar(), IntVar()
        self.check = []
        for (farbe, var) in [("rot", self.rot),
                            ("gruen", self.gruen),
                            ("blau", self.blau)]:
            self.check.append(Checkbutton(self.fenster, text=farbe, offvalue=0, onvalue=255, variable=var, command=self.mix))
        self.farbfeld = Label(self.fenster, width=20, height=6)
        self.farbfeld.pack(side=LEFT)
        for button in self.check:
            button.pack(side=RIGHT)
        self.fenster.mainloop()

    def mix(self):
        summe="#"
        for farbe in (self.rot, self.gruen, self.blau):
            summe += str(hex(farbe.get()).lstrip("0x").zfill(2))
        self.farbfeld.config(bg=summe)

farbmischer = Farbmischer()