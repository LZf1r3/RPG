#importando classe mae do arquivo itens.py
from itens import itens as it
import Itens.itens as itemlist
#Definindo food como derivada de itens e adicionando variaveis
class food(it):
    def __init__(self, name, damage, noise, tier, effect, duration):
        super().__init__(name, damage, noise, tier)
        self.effect = effect
        self.duration = duration
    
#Definindo comidas ruins tier 1:
batata_podre = food("Batata podre", 2, 2, "I", "Poison", 4 )

comida_malefica = [batata_podre]
for comida in comida_malefica:
    itemlist.adicionar_item_address(comida)
    itemlist.adicionar_item_name(comida.name)
