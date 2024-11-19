"""
Docstring
"""


def display_pair_numbers(num1: int, num2: int):
    """
    Docstring fonction display_pair_number
    """
    minimum = 0
    maximum = 0
    if num1 < num2:
        minimum = num1
        maximum = num2
    else:
        minimum = num2
        maximum = num1
    print(f"Les nombres pairs compris entre {minimum} et {maximum} sont:")
    for i in range(minimum, maximum + 1):
        if i % 2 == 0:
            print(i)


number1 = int(input("Entrer le 1er nombre\n"))
number2 = int(input("Entrer le deuxième nombre\n"))
display_pair_numbers(number1, number2)
