#importando classe mae do arquivo itens.py
from Itens.itens import itens as it
import Itens.itens as itemlist
#Definindo armaduras como derivada de itens e adicionando variaveis
class Armaduras(it):
    def __init__(self, name, damage, noise, tier, defense, weight, mana):
        super().__init__(name, damage, noise, tier)
        self.defense = defense
        self.weight = weight
        self.mana = mana

#Definindo armaduras tier 1:
mago_iniciante = Armaduras("Armadura de mago novato", 0, 2, "I", 2, 10, 25)
cavalheiro_iniciante = Armaduras("Armadura de cavalheiro caseira", 0, 6, "I", 50, 6, 0)





#Definindo armaduras tier dev:
God_armor = Armaduras("God armor", 0, 0, "GOD", 999999999, 0, 999999999)

armaduras_list = [mago_iniciante, cavalheiro_iniciante, God_armor]
for item in armaduras_list:
    itemlist.adicionar_item_address(item)
    itemlist.adicionar_item_name(item.name)
