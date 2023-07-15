#importando classe mae do arquivo itens.py
from itens import itens as it

#Definindo que venenos deriva de itens e tambem adicionando variaveis
class Venenos(it):
    def __init__(self, name, damage, noise, tier, effect, duration):
        super().__init__(name, damage, noise, tier)
        self.effect = effect
        self.duration = duration

#Definindo venenos tier 1:
veneno_I = Venenos("Veneno I", 0.05, 0, "I", "Poison", 2)
dano_instantanio_I = Venenos("Dano-Instantanio I", 10, 0, "I", "Damage", 1)

#Definindo venenos tier 2:
veneno_II = Venenos("Veneno II", 0.10, 0, "II", "Poison", 3)
dano_instantanio_II = Venenos("Dano-Instantanio II", 30, 0, "II", "Damage", 1)

#Definindo venenos tier 3:
veneno_III = Venenos("Veneno III", 0.20, 0, "III", "Poison", 4)
dano_instantanio_III = Venenos("Dano-Instantanio III", 50, 0, "III", "Damage", 1)

#enlistando venenos
venenos = [veneno_I,veneno_II,veneno_III,dano_instantanio_I,dano_instantanio_II,dano_instantanio_III]