from Personagens.personagens import personagens
class Main_Character(personagens):
    def __init__(self, name, life, damage, mana, saturation, armor):
        super().__init__(name, life, damage)
        self.mana = mana
        self.saturation = saturation
        self.armor = armor

def main_character(classe):
    from inventario.inv import wearing
    name = str(input("(Anja) Como voce gostaria de ser chamado neste novo mundo? ")).title()
    main_character = Main_Character(name, classe.life, classe.base_damage, classe.mana, 0, wearing.defense)
    print(f"Name: {main_character.name}\nLife: {main_character.life}\nMana: {main_character.mana}\nDamage: {main_character.damage}\nArmor: {main_character.armor}")
