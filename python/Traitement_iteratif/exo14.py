import random

result = random.randint(1, 30)
tryNumber = 7
currentTry = 0
playerNumber = 0

while currentTry < tryNumber and playerNumber != result:
    playerNumber = int(input("Veuillez entrer un nombre compris entre 1 et 30.\n"))
    if playerNumber > result:
        print("Trop grand")
    elif playerNumber < result:
        print("Trop petit")
    currentTry += 1

if playerNumber == result:
    print("Bravo")
else:
    print("Perdu, le nombre qu'il fallait trouver est {0}".format(result))
