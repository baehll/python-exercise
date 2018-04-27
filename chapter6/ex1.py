#####################
#   Aufgabe 1, 6.15 #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

def konkat(*strings):
    output = ""
    for item in strings:
        output += item
    print(output)
konkat("a", "b", "c", "d")
konkat("Sonnen", "schein")
