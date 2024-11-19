"""
Classe Article
"""


class Article:
    def __init__(self, code=0, nom="", quantite_stock=0, unite_vente=1):
        self.code = code
        self.nom = nom
        self.quantite_stock = quantite_stock
        self.unite_vente = unite_vente

    def AddStock(self, quantite: int):
        self.quantite_stock += quantite

    def SetUnitV(self, unite_vente):
        if unite_vente > 0:
            self.unite_vente = unite_vente

    def __str__(self):
        result = f"Code: {self.code}\n"
        result += f"Nom: {self.nom}\n"
        result += f"Quantité en stock: {self.quantite_stock}\n"
        result += f"Unité de vente: {self.unite_vente}"
        return result

    def Affiche(self):
        print(self)


"""
article = Article(123, "Boubou", 12, 5)
article.Affiche()
article.AddStock(2)
print("ajout 2 qunatite stock")
print(article)
print("modifier unite de vente àn1")
article.SetUnitV(1)
print(article)
"""
