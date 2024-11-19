"""
Docstring fichier
"""

# COmmentaire sur 1 ligne
print("Hello world!")  # On peut l'écrire en milieu de ligne


# Commentaire sur plusieurs lignes


a = 3
b = True
b = "Bonjour"
b = 6.0
print(type(b))
print(f"{a} est inférieur à {b}")

x = 8
if x > 0:
    print("a")
elif x == 0:
    print("b")
else:
    print("c")

y = 1 if (x == 0) else -1
for i in range(10):
    print("bonjour")
    if i == 3:
        break
else:
    print("Suite de code")
