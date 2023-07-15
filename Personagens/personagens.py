#Criando classe dos personagens que sera mae de todos os personagens presentes na historia (inclui monstros e animains)
class personagens:
    def __init__(self,name,life,damage):
        self.name = name
        self.life = life
        self.damage = damage



primeiro_boss = personagens("Gordon", 75, 4)
