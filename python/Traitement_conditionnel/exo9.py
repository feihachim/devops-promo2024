number1 = int(input("Entrez un premier nombre\n"))
number2 = int(input("Entrez un second nombre\n"))
number3 = int(input("Entrez un troisième nombre\n"))

if number1 == number2 + number3:
    print("{0} est égal à la somme de {1} et {2}".format(number1, number2, number3))
elif number2 == number1 + number3:
    print("{0} est égal à la somme de {1} et {2}".format(number2, number1, number3))
elif number3 == number1 + number2:
    print("{0} est égal à la somme de {1} et {2}".format(number3, number1, number2))
else:
    print("Il n'y a pas de nombre qui soit égal à la somme des 2 autres nombres")
