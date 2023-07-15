from Personagens.personagens import personagens
class Main_Character_class(personagens):
    def __init__(self, name, life, damage, mana, saturation, armor, mana_armor):
        super().__init__(name, life, damage)
        self.mana = mana
        self.saturation = saturation
        self.armor = armor
        self.mana_armor = mana_armor
        self.inventario = []

def Main_character(classe):
    from inventario.inv import em_uso
    name = str(input("(Anja) Como voce gostaria de ser chamado neste novo mundo? ")).title()
    main_character = Main_Character_class(name, classe.life, classe.base_damage, classe.mana, 0, em_uso.defense, em_uso.mana)
    print(f"Name: {main_character.name}\nLife: {main_character.life}\nMana: {main_character.mana}\nDamage: {main_character.damage}\nArmor: {main_character.armor}\nArmor-Mana: {main_character.mana_armor}")
