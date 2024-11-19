"""
Classe stock
"""

from typing import Type, Self
from article import Article


class Stock:
    def __init__(self):
        self.liste = []

    def copy(self, liste=[]):
        self.liste = liste

    def Add_art(self, article: Article):
        duplicate_articles = list(
            filter(lambda x: x.code == article.code or x.nom == article.nom, self.liste)
        )
        if len(duplicate_articles) == 0:
            self.liste.append(article)
            self.liste.sort(key=lambda x: x.code)

    def Get_Stock(self, code: int):
        article = list(filter(lambda x: x.code == code, self.liste))
        if len(article) == 1:
            return article[0].quantite_stock
        return -1

    def Supprime(self, code: int):
        if self.Get_Stock(code):
            articles_restants = list(filter(lambda x: x.code != code, self.liste))
            self.copy(articles_restants)

    @staticmethod
    def __filtrer_liste_par_code(liste: list[Type[Article]]) -> list[Type[Article]]:
        index_liste = 0
        liste_fusionnee = []
        while index_liste < len(liste) - 1:
            current = liste[index_liste]
            next_item = liste[index_liste + 1]
            if current.code == next_item.code:
                if current.nom == next_item.nom:
                    nom = current.nom
                else:
                    nom = f"{current.nom}_{next_item.nom}"
                quantite_stock = current.quantite_stock + next_item.quantite_stock
                unite_vente = min(current.unite_vente, next_item.unite_vente)
                article = Article(current.code, nom, quantite_stock, unite_vente)
                liste_fusionnee.append(article)
                index_liste += 2
            else:
                liste_fusionnee.append(current)
                index_liste += 1
        if index_liste == len(liste) - 1:
            liste_fusionnee.append(liste[index_liste])
        return liste_fusionnee

    @staticmethod
    def __filtrer_liste_par_nom(liste: list[Type[Article]]) -> list[Type[Article]]:
        index_liste = 0
        liste_filtree = []
        while index_liste < len(liste) - 1:
            current_item = liste[index_liste]
            next_item = liste[index_liste + 1]
            if current_item.nom in next_item.nom or next_item.nom in current_item.nom:
                code = min(current_item.code, next_item.code)
                if len(current_item.nom) > len(next_item.nom):
                    nom = current_item.nom
                else:
                    nom = next_item.nom
                quantite_stock = current_item.quantite_stock + next_item.quantite_stock
                unite_vente = min(current_item.unite_vente, next_item.unite_vente)
                article = Article(code, nom, quantite_stock, unite_vente)
                liste_filtree.append(article)
                index_liste += 2
            else:
                liste_filtree.append(current_item)
                index_liste += 1
        if index_liste == len(liste) - 1:
            liste_filtree.append(liste[index_liste])
        return liste_filtree

    @staticmethod
    def Fusionner_listes(
        liste1: list[Type[Article]], liste2: list[Type[Article]]
    ) -> Self:
        """_summary_

        Args:
            stock1 (list): _description_
            stock2 (list): _description_
        """
        liste_initiale = []
        liste_initiale.extend(liste1)
        liste_initiale.extend(liste2)
        liste_initiale.sort(key=lambda x: x.code)
        liste_par_code = Stock.__filtrer_liste_par_code(liste_initiale)
        liste_par_code.sort(key=lambda x: x.nom)
        liste_par_nom = Stock.__filtrer_liste_par_nom(liste_par_code)
        liste_finale = sorted(liste_par_nom, key=lambda x: x.code)
        stock_fusion = Stock()
        stock_fusion.liste = liste_finale
        return stock_fusion

    def Affiche(self):
        print("=============================================")
        print("------------------------------------")
        for article in self.liste:
            print(article)
            print("------------------------------------")
        print("=============================================")

    def Approvisionner(self, article: Article, quantite: int):
        if self.Get_Stock(article.code):
            index_article = self.liste.index(article)
            self.liste[index_article].quantite_stock += quantite

    def Vente(self, article: Article, quantite: int):
        if self.Get_Stock(article.code):
            try:
                index_article = self.liste.index(article)
                article_dans_liste = self.liste[index_article]
                quantite_restante = article_dans_liste.quantite_stock - quantite
                if (
                    quantite_restante % article_dans_liste.unite_vente == 0
                    and quantite_restante >= 0
                ):
                    return True
            except:
                return False
        return False


article1 = Article(1, "boubou", 3, 45)
article2 = Article(2, "baba", 2, 6)
article3 = Article(4, "bibi", 5, 15)
article4 = Article(1, "boubou", 7, 21)
article5 = Article(3, "bebe", 9, 18)
article6 = Article(4, "baba", 11, 22)
article7 = Article(5, "bibi", 8, 16)
article8 = Article(7, "bubu", 6, 24)

stock1 = Stock()
stock2 = Stock()

stock1.Add_art(article1)
stock1.Add_art(article2)
stock1.Add_art(article3)
stock2.Add_art(article4)
stock2.Add_art(article5)
stock2.Add_art(article6)
stock2.Add_art(article7)
stock2.Add_art(article8)

stock_fusionne = Stock.Fusionner_listes(stock1.liste, stock2.liste)
print("stock 1")
stock1.Affiche()
print("========================")
print("stock 2")
stock2.Affiche()
print("========================")
print("stock fusionné")
stock_fusionne.Affiche()
