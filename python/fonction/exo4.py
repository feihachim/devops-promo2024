"""
Factorielle fonction
"""


def factorielle(num: int) -> int:
    """
    Factorielle entier
    """
    if num < 0:
        return 0
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


number = int(input("Entrer un nombre\n"))
resultat = factorielle(number)
print(f"La factorielle de {number} vaut {resultat}")
