print(
    "Veuillez entrer les 3 nombres réels a,b etc de l'équation du second degré ax^2+bx+c=0"
)
a = float(input("Le nombre a\n"))
b = float(input("Le nombre b\n"))
c = float(input("Le nombre c\n"))

print("L'équation qu'on va résoudre est {0}x^2 + {1}x + {2} = 0".format(a, b, c))

delta = b**2 - (4 * a * c)

print("On calcule le discriminant qui vaut b^2-4ac et on a delta={0}".format(delta))

if delta > 0:
    x1 = (-b - delta**0.5) / (2 * a)
    x2 = (-b + delta**0.5) / (2 * a)
    print(
        "Le discriminant est positif donc l'équation a 2 solutions réelles x1={0:.2f} et x2={1:.2f} ".format(
            x1, x2
        )
    )

elif delta == 0:
    x = -b / (2 * a)
    print(
        "Le discriminant est nul donc l'équation a une solution réelle x={0:.2f}".format(
            x
        )
    )

else:
    l = 1j
    posDelta = -delta
    x1 = (-b - (l * (posDelta**0.5))) / 2 * a
    x2 = (-b + (l * (posDelta**0.5))) / 2 * a
    print(
        "Le discriminant est négatif donc l'équation a deux solutions complexes x1={0:.2f} et x2={1:.2f}".format(
            x1, x2
        )
    )
