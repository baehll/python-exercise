#####################
#   Aufgabe 1, 20.3 #
#   v1.0            #
#   baehll          #
#   15.05.2018      #
##################### 
from tkinter import *
from time import *
from _thread import *

import tkinter, time, _thread

class Timer:
    def __init__(self):
        self.container = Tk()
        self.zeitVar = StringVar()
        self.zeitLabel = Label(master=self.container, textvariable=self.zeitVar, font=("Arial", 20))
        self.zeitLabel.pack()
        _thread.start_new_thread(self.aktualisieren, ())
        self.container.mainloop()

    def aktualisieren(self):
        while True:
            self.zeitVar.set(strftime("%X"))
            sleep(1)


t = Timer()