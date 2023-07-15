#Criando classe mae de todas a coisas presentes no rpg
class itens:
    def __init__(self, name, damage, noise, tier):
        self.name = name
        self.damage = damage
        self.noise = noise
        self.tier = tier