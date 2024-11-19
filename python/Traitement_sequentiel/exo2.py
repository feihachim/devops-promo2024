number1 = int(input("Veuillez entrer un premier entier \n"))
number2 = int(input("Veuillez entrer le second entier \n"))
number3 = int(input("Veuillez enter le drenier entier \n"))

print("Le carré de {0} est {1}".format(number1, number1**2))
print("Le carré de {0} est {1}".format(number2, number2**2))
print("Le carré de {0} est {1}".format(number3, number3**2))

print("La somme de ces nombres est égale à {0}".format(number1 + number2 + number3))
print(
    "La moyenne de ces 3 nombres est égale à {0}".format(
        round((number1 + number2 + number3) / 3, 2)
    )
)
