number = int(input("Entrez un nombre entier positif ou nul\n"))

factorielle = 1
for i in range(1, number + 1):
    factorielle *= i

print("La factorielle de {0} est {1}".format(number, factorielle))
