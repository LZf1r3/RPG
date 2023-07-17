from Personagens.personagens import personagens
import Itens.armamentos.armaduras as arms
class bosses(personagens):
    def __init__(self, name, life, damage,drops):
        super().__init__(name, life, damage)
        self.drops = drops
    
first_boss = bosses("Gordon",75,4,[arms.cavalheiro_iniciante,arms.feral_iniciante])
