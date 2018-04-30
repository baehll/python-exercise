#####################
#   Aufgabe 3, 10.11#
#   v1.0            #
#   baehll          #
#   30.04.2018      #
#####################

class NewList(list):
    def __init__(self, l):
        list.__init__(self, l)
    
    def range(self):
        return self[-1] - self[0]

n = NewList([1, 2, 3, 4, 5])

print(n.range())