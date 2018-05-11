from tkinter import *

class Spielflaeche:
    def __init__(self):
        self.fenster = Tk()
        self.canvas = Canvas(self.fenster, width="10c", height="5c")
        self.canvas.pack()
        h = PhotoImage(file="/python/gemini/erde.gif")
        self.canvas.create_image(0, 0, anchor=NW, image=h)
        g7 = PhotoImage(file="/python/gemini/gemini7d.gif")
        self.gemini7 = self.canvas.create_image(50, 50, image=g7)
        g6 = PhotoImage(file="/python/gemini/gemini6.gif")
        self.canvas.create_image(300, 30, image=g6)
        self.fenster.bind("<KeyPress-Down>", func=self.down)
        self.fenster.bind("<KeyPress-Up>", func=self.up)
        self.fenster.bind("<KeyPress-Left>", func=self.left)
        self.fenster.bind("<KeyPress-Right>", func=self.right)
        self.fenster.mainloop()

    def up(self, event):
        self.canvas.move(self.gemini7, 0, -3)

    def down(self, event):
        self.canvas.move(self.gemini7, 0, +3)
    
    def left(self, event):
        self.canvas.move(self.gemini7, -3, 0)
    
    def right(self, event):
        self.canvas.move(self.gemini7, +3, 0)

s = Spielflaeche()