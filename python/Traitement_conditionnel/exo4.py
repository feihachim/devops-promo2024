pSeuil = 2.3
vSeuil = 7.41

pCurrent = float(input("Veuillez entrer la pression courante de l'enceinte\n"))
vCurrent = float(input("Veuillez enter le volume courant de l'enceinte\n"))

print("Exercice 4")
if pCurrent > pSeuil and vCurrent > vSeuil:
    print("Arret immédiat")
elif pCurrent > pSeuil:
    print("Augmenter le volume de l'enceinte")
elif vCurrent > vSeuil:
    print("Diminuer le volume de l'enceinte")
else:
    print("Tout va bien")
