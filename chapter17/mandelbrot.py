from tkinter import *

RADIUS = 2.0
ZOOM = 150.0

class Mandelbrot:
    def __init__(self):
        self.fenster = Tk()
        self.bild = PhotoImage(width=600, height=400)
        self.bildflaeche = Label(master=self.fenster, image=self.bild)
        self.bildflaeche.pack()
        self.__zeichnen()
        self.fenster.mainloop()
    
    def __zeichnen(self):
        intervall = [x/ZOOM for x in range(-200, 200)]
        mandelbrot = [(x, y) for x in intervall
                            for y in intervall
                            if self.__test(x, y)]

        for x, y in mandelbrot:
            self.bild.put("#0000ff", (int(ZOOM*x+200), int(ZOOM*y+200)))
    
    def __test(self, x, y):
        c = x + 1j * y
        z = 0
        for i in range(20):
            if abs(z) < RADIUS:
                z = z * z - c
            else:
                return False
        return True

m = Mandelbrot()