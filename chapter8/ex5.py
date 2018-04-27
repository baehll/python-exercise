#####################
#   Aufgabe 5, 8.6  #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

def haeufigkeiten(string):
    d = {}
    for key in string:
        d[key] = string.count(key)
    return d
    
print(haeufigkeiten("Erdbeereis"))

