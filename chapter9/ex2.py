#####################
#   Aufgabe 2, 9.7  #
#   v1.0            #
#   baehll          #
#   29.04.2018      #
#####################

liste = [("Gold", 0.1234), ("Silber", 23.45), ("Platin", 0.0678)]

for item in liste:
    print(item[0], str(item[1]), sep=" ", end=" // ")

print("")

for item in liste:
    print(item[0], item[1], sep="\t")

print("")
for item in liste:
    print(item[0] + ":", format(item[1], "8.2f"), sep="\t")