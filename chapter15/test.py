from tkinter import *

fenster = Tk()

gruss = StringVar()
engl = Radiobutton(fenster, text="englisch      ", value="Hello", variable=gruss)
franz = Radiobutton(fenster, text="franzoesisch ", value="Bonjour", variable=gruss)
deutsch = Radiobutton(fenster, text="deutsch    ", value="Hallo", variable=gruss)
ausgabe = Label(fenster, textvariable=gruss, font=("Arial", 20), width=10)

deutsch.select()
ausgabe.pack()
franz.pack()
engl.pack()
deutsch.pack()

fenster.mainloop()