heures = int(input("Entrez un nombre d'heures compris entre 0 et 23\n"))
minutes = int(input("Entrez un nombre de minutes compris entre 0 et 59\n"))
secondes = int(input("Entrez un nombre de secondes compris entre 0 et 59\n"))

secondes += 1
if secondes == 60:
    secondes = 0
    minutes += 1
    if minutes == 60:
        minutes = 0
        heures += 1
        if heures == 24:
            heures = 0

print(
    "Si on ajoute 1 seconde, le nouveau temps est {0} heures, {1} minutes et {2} secondes".format(
        heures, minutes, secondes
    )
)
