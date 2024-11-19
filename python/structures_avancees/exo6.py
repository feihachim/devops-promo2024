"""
Exercice sur les dictionnaires
"""

ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}

# Somme totale des ventes de la société
tab_ventes = ventes.values()
total_ventes = sum(tab_ventes)
print(f"La somme totale des ventes vaut {total_ventes}")

# Vendeur ou vendeurs ayant réalisé le plus de ventes
max_ventes = max(tab_ventes)
meilleur_vendeur = []

for key, value in ventes.items():
    if value == max_ventes:
        meilleur_vendeur.append(key)

print(f"meilleurs vendeurs: {meilleur_vendeur}")
