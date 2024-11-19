"""
Docstring fonction multiple
"""


def multiple_number(num):
    """
    Fonction multiple d'un nombre
    """
    for i in range(0, 11):
        print(f"{num}*{i}={num * i}")


number = int(input("Entrer un nombre entier positif\n"))
multiple_number(number)
