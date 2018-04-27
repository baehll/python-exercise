#####################
#   Aufgabe 5, 6.15 #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################
from turtle import *

def baum1(x):
    if(x <= 5): return
    fd(x)
    left(30)
    baum1(0.7*x)
    right(90)
    baum1(x/2)
    left(60)
    back(x)
    return

left(90)
baum1(100)
hideturtle()

input()
