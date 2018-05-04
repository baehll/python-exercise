from tkinter import *

def gruessen():
    fenster.label.config(text="Hallo")

fenster = Tk()
fenster.label = Label(fenster, text="Begrüßung")
fenster.label.pack()
fenster.button = Button(fenster, text="Sag Hallo", command=gruessen)
fenster.button.pack()
fenster.mainloop()