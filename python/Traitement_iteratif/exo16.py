"""
Docstring du fichier
"""


def rectangle(num: int):
    """
    fonction rectangle
    """
    print("*" * 2 * num)
    if num > 1:
        i = 2
        while i < num:
            print("*" + 2 * (num - 1) * " " + "*")
            i += 1
        print("*" * 2 * num)


def triangle_rectangle(num: int):
    """
    Fonction triangle rectangle
    """
    line = ""
    for i in range(1, num + 1):
        line = "*" * i
        print(line)


def triangle(num):
    """
    fonction triangle
    """
    line = ""
    for i in range(1, num + 1):
        line = (num - i) * " " + (2 * i - 1) * "*"
        print(line)


number = input("Entrer un nombre\n")

value = int(number)
rectangle(value)
print("------------------------------------")
triangle_rectangle(value)
print("------------------------------------")
triangle(value)
