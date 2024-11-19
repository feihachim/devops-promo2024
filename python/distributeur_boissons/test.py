import datetime
from typing import Self

liste = [9, 7, 3, 1, 5]

test_pair = list(filter(lambda x: x % 2 == 0, liste))
print("taille", len(test_pair))
for item in test_pair:
    print(item)
filter_list = test_pair
print("type test_pair", type(filter_list))
print("test_pair", test_pair)
liste.sort(key=lambda x: x)
print("liste triee", liste)
date_today = datetime.datetime.now()
print("type date_today", type(date_today))
vente = f"{date_today}"
print("type vente", type(vente))
print("vente", vente)
elo = date_today.date()
print("date sans heure", elo)
heure = datetime.datetime.now().hour
print("heure", heure)
gelo = f"{elo}_{heure}h"
print(gelo)


class trial:
    def __init__(self, num1: int):
        self.num1 = num1


class test:
    def __init__(self, trial: type[trial], liste: list[Self] = []):
        self.trial = trial
        self.liste = liste
