from tkinter import *

class Raster:
    def __init__(self):
        liste = [(x, y) for x in range(20)
                        for y in range(20)]
        self.fenster = Tk()
        for (i, j) in liste:
            l = Label(self.fenster, width=2, height=1, bg="white")
            l.grid(column=i, row=j)
            l.bind(sequence="<Button-1>", func=self.leftclick)
            l.bind(sequence="<Button-3>", func=self.rightclick)
            l.bind(sequence="<Double-Button-1>", func=self.doubleclick)
        self.fenster.mainloop()

    def leftclick(self, event):
        event.widget.config(bg="black")
    
    def rightclick(self, event):
        event.widget.config(bg="grey")
    
    def doubleclick(self, event):
        event.widget.config(bg="white")

r = Raster()