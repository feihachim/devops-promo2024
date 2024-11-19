import random

somme = 0
sommeTotale = 0
score1 = 0
score2 = 0

turnNumber = int(input("Combien de tours allez-vous jouer?\n"))
if turnNumber < 0 or not isinstance(turnNumber, int):
    print("Erreur: Entrez un nombre entier positif")
    exit()

for turn in range(1, turnNumber + 1):
    score1 = random.randint(1, 6)
    score2 = random.randint(1, 6)
    somme = score1 + score2
    sommeTotale += somme
    print(f"Au tour {turn}")
    print("Le joueur 1 a fait {0}".format(score1))
    print(f"Le joueur 2 a fait {score2}")
    print("La somme au tour {0} est {1}".format(turn, somme))
    print("-----------------------------------------------")


print(f"La somme totale est {sommeTotale}")
if sommeTotale % 2 == 0:
    print("Le joueur 1 a gagné")
else:
    print("Le joueur 2 a gagné")
