print("Voici les nombres qui sont divisibles par 3 et non divisibles par 5")
for number in range(1, 201):
    if number % 3 == 0 and number % 5 != 0:
        print(number)
