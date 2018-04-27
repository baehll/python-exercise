#####################
#   Aufgabe 3, 6.15 #
#   v1.0            #
#   baehll          #
#   27.04.2018      #
#####################

def wurzel(x, n=10):
    if (n == 1): return 1
    return 0.5*(wurzel(x, n - 1) + x / wurzel(x, n-1))

print(wurzel(100))