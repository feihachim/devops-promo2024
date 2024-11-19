"""
Structures avancées exercice 1
"""

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def pair(num):
    """
    fonction pair
    """
    return num % 2 == 0


def impair(num):
    """
    fonction impaire
    """
    return num % 2 == 1


# Ajouter 1 à chaque élément de la liste
for index, value in enumerate(L):
    L[index] = value + 1

print(L)

# Ajouter 11 à la fin de la liste
L.append(11)
print(L)

# Ajouter 12 et 13 à la fin de la liste
L.extend([12, 13])
print(L)

# Afficher le premier élément
print(L[0])

# Afficher les 2 premiers éléments
print(L[0:2])

# Afficher le dernier élément
print(L[-1])

# Afficher les deux derniers éléments
print(L[-2:])

# Afficher la liste paire
pairList = filter(pair, L)
print(list(pairList))

# Afficher la liste imapire
impairList = filter(impair, L)
print(list(impairList))

# Ajouter la valeur 3.5 entre 3 et 4
index = 0
while L[index] < 3.5 and index < len(L):
    index += 1

L.insert(index, 3.5)
print(L)

# Supprimer la valeur 3.5
L.remove(3.5)
print(L)

# Inverser l'ordre des éléments de L
L.reverse()
print(L)

# Demander à l'utilisateur de fournir un nombre au hasard et dire si ce nombre est présent dans L
nombre = int(input("Veuillez entrer un nombre\n"))
nombre_element = L.count(nombre)
if nombre_element == 0:
    print(f"{nombre} n'est pas présent dans L")
else:
    print(f"{nombre} est présent dans L")

# Trier la liste
L.sort()
print(L)

# Déterminer le plus petit et le plus grand élément
minimum = min(L)
maximum = max(L)
print(f"{minimum} est le plus petit élément de L")
print(f"{maximum} est le plus grand élément de L")

# Calculer la somme des éléments de la liste
somme = sum(L)
print(f"La somme des éléments de L vaut {somme}")
