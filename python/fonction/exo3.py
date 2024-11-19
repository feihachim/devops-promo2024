"""
Fonction est nombre premier
"""


def is_prime_number(num: int) -> bool:
    """
    Fonction is_prime_number
    """
    if num == 1:
        return False
    if num == 2:
        return True
    counter = 2
    limit = round(num**0.5)
    while counter < limit and num % counter != 0:
        counter += 1
    if num % counter == 0:
        return False
    return True


number = int(input("Veuillez entrer un nombre\n"))

RESULT = is_prime_number(number)
if RESULT:
    print(f"{number} est un nombre premier")
else:
    print(f"{number} n'est pas un nombre premier")
