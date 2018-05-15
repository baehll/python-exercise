import sys
from tkinter import *
import _thread

class Ausgabe:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.geometry("200x150+10+10")
        self.fenster.title("Ausgabe")
        self.text = Text(master=self.fenster, wrap=WORD, font=("Courier", 10))
        self.text.pack(expand=1)
    
    def write(self, s):
        self.text.insert(END, s)


class Editor:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.geometry("250x150+240+10")
        self.text = Text(master=self.fenster, wrap=WORD, font=("Courier", 10))
        self.text.pack(expand=1)
        self.initMenu()
        self.ausgabe = Ausgabe()
        sys.stdout = sys.stderr = self.ausgabe

    def initMenu(self):
        self.menueleiste = Menu(self.fenster)
        self.fenster.configure(menu=self.menueleiste)
        self.menue = Menu(master=self.menueleiste)
        self.menueleiste.add_cascade(label="Befehle", menu=self.menue)
        self.menue.add_command(label="Programm starten (F5)", command=self.startenThread)
        self.menue.add_command(label="Ende", command=self.beenden)
        
    def startenThread(self):
        _thread.start_new_thread(self.starten, ())

    def starten(self):
        programmtext = self.text.get(1.0, END)
        exec(programmtext)
    
    def beenden(self):
    
        if messagebox.askyesno("Beenden", "Wollen sie wirklich das Programm beenden?"):
            self.ausgabe.fenster.destroy()
            self.fenster.destroy()

editor = Editor()
mainloop()