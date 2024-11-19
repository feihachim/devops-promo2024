number1 = int(input("Entrer un premier nombre\n"))
number2 = int(input("Entrer un deuxième nombre\n"))
number3 = int(input("Entrer un dernier nombre\n"))

minimum = number1
if number2 < minimum:
    minimum = number2
if number3 < minimum:
    minimum = number3

print("Le plus petit des 3 nombres est {0}".format(minimum))
