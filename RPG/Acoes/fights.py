import Personagens.Main_character as MC
import Personagens.Bosses as bosses

def fight(who,against_who):
    if who.life >= against_who.life:
        print(f"{who.name} e mais forte que {against_who.name}")
    else:
        print(f"{who.name} e mais fraco que {against_who.name}")
