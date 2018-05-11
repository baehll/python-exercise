#####################
#   Aufgabe 1, 16.5 #
#   v1.0            #
#   baehll          #
#   11.05.2018      #
#####################

from tkinter import *
from random import *

class SchiffeVersenken(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.spielfeld = Spielfeld()
        self.title("Schiffe Versenken")
        for i in range(12):
            for j in range(12):
                button=Feld(self, i, j)
        
        self.mainloop()

class Feld:
    def __init__(self, master, i, j):
        self.x = i
        self.y = j
        self.field = master
        self.button = Button(master=self.field, text="  ", command=self.press, bg="blue")
        self.button.grid(column=self.x, row=self.y)

    def press(self):
        check = self.field.spielfeld.checkTreffer
        if check(self.x, self.y):
            self.button.config(bg="red")
        else:
            self.button.config(bg="white")

class Spielfeld:
    def __init__(self):
        self.d = {}
        for i in range(12):
            for j in range(12):
                self.d[(i, j)] = 0
        for i in range(4):
            self.setzeBoot(1)
        for i in range(3):
            self.setzeBoot(2)
        for i in range(2):
            self.setzeBoot(3)
        self.setzeBoot(4)

    def setzeBoot(self, laenge):
        max = 11 - laenge
        ok = 0
        while not ok:
            if choice([0, 1]):
                y = randint(1, 10)
                x = randint(1, max)
                if self.check(x, y, x+laenge-1, y):
                    for x in range(x, x+laenge):
                        self.d[x, y] = 1
                    ok = 1
            else:
                y = randint(1, max)
                x = randint(1, 10)
                if self.check(x, y, x, y+laenge-1):        
                    for y in range(y, y+laenge):
                        self.d[(x, y+laenge)] = 1
                    ok = 1
    
    def check(self, x1, y1, x2, y2):
        ok = 1
        for x in range(x1-1, x2+2):
            for y in range(y1-1, y2+2):
                if self.d[x, y]: ok = 0
        return ok
    
    def checkTreffer(self, x, y):
        return self.d[x, y]


if __name__ == "__main__":
    s = SchiffeVersenken()