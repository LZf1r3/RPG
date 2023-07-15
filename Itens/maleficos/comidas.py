#importando classe mae do arquivo itens.py
from itens import itens as it

#Definindo food como derivada de itens e adicionando variaveis
class food(it):
    def __init__(self, name, damage, noise, tier, effect, duration):
        super().__init__(name, damage, noise, tier)
        self.effect = effect
        self.duration = duration
    
#Definindo comidas ruins tier 1:
batata_podre = food("Batata podre", 2, 2, "I", "Poison", 4 )
