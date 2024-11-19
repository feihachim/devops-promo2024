"""
Projet Distributeur de boissons
"""

import json
import os
import sys
import datetime

working_directory = os.path.dirname(os.path.realpath(__file__))
SEPARATOR = "\\"
TEXT_FILE = "menu.json"
LOG_DIRECTORY = "Distr"
LOG_FILE = "log"

full_path_text_file = f"{working_directory}{SEPARATOR}{TEXT_FILE}"
full_path_log_file = (
    f"{working_directory}{SEPARATOR}{LOG_DIRECTORY}{SEPARATOR}{LOG_FILE}"
)

with open(full_path_text_file, "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

boissons = data["products"]
prix = data["prices"]
pieces_acceptees = tuple(data["pieces"])


def afficher_menu(liste_boissons: dict, liste_prix: dict):
    """_summary_

    Args:
        liste_boissons (dict): _description_
        liste_prix (dict): _description_
    """
    liste_taille_boissons = []
    for element in liste_boissons.values():
        liste_taille_boissons.append(len(element))
    maximum_taille_mots = max(liste_taille_boissons)
    liste_taille_prix = []
    for element in liste_prix.values():
        liste_taille_prix.append(len(str(element)))
    maximum_taille_prix = max(liste_taille_prix)
    liste_menu = []

    for i in liste_boissons:
        nombre_points = (maximum_taille_mots - len(liste_boissons[i]) + 3) * "."
        nombre_espaces = (maximum_taille_prix - len(str(liste_prix[i])) + 1) * " "
        item = f"{i}.{liste_boissons[i]} {nombre_points} ({nombre_espaces}{liste_prix[i]} P )"
        liste_menu.append(item)

    for item in liste_menu:
        print(item)

    print("0.Annuler")


def rendre_monnaie(montant: int) -> list:
    """_summary_

    Args:
        montant (int): _description_

    Returns:
        list: _description_
    """
    nombre_pieces = []
    reste = montant
    i = 0
    while reste > 0 and i < len(pieces_acceptees):
        piece = reste // pieces_acceptees[i]
        nombre_pieces.append(piece)
        reste = reste % pieces_acceptees[i]
        i += 1
    return nombre_pieces


def afficher_monnaie(tab_monnaie: list):
    """_summary_

    Args:
        tab_monnaie (list): _description_
    """
    result = "La monnaie est de "
    for index, value in enumerate(tab_monnaie):
        if value > 0:
            result += f"{value} pièces de {pieces_acceptees[index]} P, "
    print(result[:-2])


def main():
    """_summary_"""
    somme = 0
    piece = 0
    afficher_menu(boissons, prix)
    choix = input("Sélectionnez votre boisson\n")
    if choix == "0":
        print("Dommage")
        sys.exit()
    print(f"Vous avez choisi un {boissons[choix]}. Merci de payer {prix[choix]} P.")
    print("Merci d'introduire les pièces de monnaie")
    while somme < prix[choix]:
        piece = input("")
        somme += int(piece)
    print(f"Montant saisi = {somme} P")
    if somme == prix[choix]:
        print("Rendu = 0 P")
    else:
        nombre_pieces = rendre_monnaie(somme - prix[choix])
        print(f"Rendu = {somme-prix[choix]}")
        afficher_monnaie(nombre_pieces)
    print("Votre boisson est prête !")
    date_du_jour = datetime.datetime.now()
    nouvelle_vente = f"{date_du_jour};{boissons[choix]}\n"
    with open(full_path_log_file, "a") as log_file:
        log_file.write(nouvelle_vente)


def filtrer_vente(ligne_vente: str, date: str, item: str) -> bool:
    split_ligne = ligne_vente.split(";")
    if date in split_ligne[0] and item in split_ligne[1]:
        return True
    return False


def recap_jour():
    somme = 0
    with open(full_path_log_file, "r") as fichier_ventes:
        liste_ventes = fichier_ventes.readlines()

    full_date_du_jour = datetime.datetime.now()
    date_du_jour = full_date_du_jour.date()
    heure_du_jour = full_date_du_jour.hour
    recap_file = f"{date_du_jour}_{heure_du_jour}h.txt"
    full_path_recap_file = (
        f"{working_directory}{SEPARATOR}{LOG_DIRECTORY}{SEPARATOR}{recap_file}"
    )
    with open(full_path_recap_file, "w") as recap_file_now:
        for index in boissons:
            filtered_list = [
                element
                for element in liste_ventes
                if filtrer_vente(element, str(date_du_jour), boissons[index])
            ]
            nom_produit = boissons[index]
            prix_produit = len(filtered_list) * prix[index]
            somme += prix_produit
            recap_file_now.write(f"{nom_produit} {prix_produit}\n")
        recap_file_now.write(f"Recette du jour: {somme}\n")


while True:
    main()
    print(
        "Voulez-vous une autre boisson? Tapez O ou o pour Oui,toute autre réponse pour non"
    )
    reponse = input()
    if reponse not in ("O", "o"):
        recap_jour()
        sys.exit()
