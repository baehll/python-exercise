#####################
#   Aufgabe 1, 16.5 #
#   v2.0            #
#   baehll          #
#   11.05.2018      #
#####################

from tkinter import *
from random import *

class Graubraten():
    def __init__(self):
        self.frame = Tk()
        self.inputContainer = Frame(master=self.frame)
        self.randomGrayLabel = Label(master=self.frame, width=2, height=8)
        self.setRandomGray()
        self.userGrayLabel = Label(master=self.frame, bg="#000000", width=2, height=8)

        self.brightnessScale = Scale(master=self.inputContainer, to=255, command=self.updateUserGray, orient=HORIZONTAL, label="Helligkeit", showvalue=0, length=255)
        self.checkButton = Button(master=self.inputContainer, text="Check", command=self.compareGray)

        self.feedbackLabel = Label(master=self.inputContainer, text="Regler verschieben\nund den Button drücken")

        self.packer()
        self.frame.mainloop()

    def packer(self):
        self.randomGrayLabel.pack(anchor=NW, side=LEFT)

        self.userGrayLabel.pack(anchor=NE, side=RIGHT)

        self.brightnessScale.pack(padx=1, pady=1)
        self.checkButton.pack(padx=1, pady=1)
        self.feedbackLabel.pack(padx=1, pady=1)
        self.inputContainer.pack(padx=5, pady=5, anchor=N, side=TOP)

    def compareGray(self):
        randomGray = self.randomGrayLabel.cget("bg")
        userGray = self.userGrayLabel.cget("bg")
        if randomGray == userGray:
            self.feedbackLabel.config(text="Richtig")
        elif randomGray > userGray:
            self.feedbackLabel.config(text="Zu dunkel")
        elif randomGray < userGray:
            self.feedbackLabel.config(text="Zu hell")

    def updateUserGray(self, event):
        userGray = hex(self.brightnessScale.get())
        hexGray = str(userGray).lstrip("0x").zfill(2)
        self.userGrayLabel.config(bg="#" + 3 * hexGray)

    def setRandomGray(self):
        range_ = "0123456789ABCDEF"
        gray = choice(range_) + choice(range_)
        self.randomGrayLabel.config(bg="#" + 3 * gray)

    
g = Graubraten()