annee = int(input("Veuillez entrer une année\n"))

if annee % 4 == 0 and annee % 100 != 0:
    print("{0} est une année bissextile".format(annee))
elif annee % 400 == 0:
    print("{0} est une année bissextile".format(annee))
else:
    print("{0} n'est pas une année bissextile".format(annee))
