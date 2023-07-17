class Classes:
    def __init__(self, name, damage, life, mana, noise, info):
        self.name = name
        self.base_damage = damage
        self.life = life
        self.mana = mana
        self.info = info
        self.noise = noise

#!!!!!Funcao criada sem utilizacao / OBS.:(Verificar utilidade da funcao antes de exclui-la)
    #def information(classe_name):
        #classes = [draconico,elfo,feral,mago]
        #for classe in classes:
            #if classe.name == classe_name:
                #print(classe.info)

#Criando variaveis de leitura do arquivo txt das classes onde tem a informacao necessaria delas
drac_file = open("RPG/Classes_folder/Classes_info_folder/Draconico.txt","r")
elfo_file = open("RPG/Classes_folder/Classes_info_folder/Elfo.txt","r")
fera_file = open("RPG/Classes_folder/Classes_info_folder/Feral.txt","r")
mago_file = open("RPG/Classes_folder/Classes_info_folder/Mago.txt","r")

#Definindo as classes
draconico = Classes("Draconico", 7, 125, 25, 10,drac_file.read())
elfo = Classes("Elfo", 4.5, 80, 75, 2, elfo_file.read())
feral = Classes("Feral", 8.5, 145, 0, 10, fera_file.read())
mago = Classes("Mago", 5, 100, 100, 4, mago_file.read())

#Criando lista das classes que e mto importante 
num_classes = [draconico,elfo,feral,mago]

#Funcao de escrever classes em um txt
def writing_classes():
        for classe in num_classes:
            with open("RPG/Classes_folder/Playable_classes.txt","r") as file_r:
                if f"{classe.name}\n" in file_r.readlines():
                    print(f"A classe {classe.name} ja esta salva!")
                else:
                     with open("RPG/Classes_folder/Playable_classes.txt","a") as file_w:
                          file_w.write(f"{classe.name}\n")

class Main_character_class():
    def __init__(self, classe,vida, dano, mana, saturacao, armadura, armadura_mana):
        self.nome = str(input("Como voce gostaria de se chamar neste novo mundo? "))
        self.classe = classe
        self.vida = vida
        self.dano = dano
        self.mana = mana
        self.saturacao = saturacao
        self.armadura = armadura
        self.armadura_mana = armadura_mana
        self.inventario = []

qual_classe = str(input("Digite o nome da classe ou digite 'help' para saber as informacoes sobre uma determinada classe.\n")).strip().title()
for classe in num_classes:
    with open("RPG/Classes_folder/Playable_classes.txt","r") as file:
        if f"{qual_classe}" in file.readlines:
            if qual_classe == classe.name:
                player = Main_character_class(qual_classe,classe.life,classe.base_damage,classe.mana,0,2,3)
                print(f"Player:{player.nome}\nClasse:{player.classe}\nVida:{player.vida}\nDano:{player.dano}\nMana:{player.mana}\nSaturacao:{player.saturacao}\nArmadura-mana:{player.armadura_mana}\nArmadura-defesa:{player.armadura}")
        else:
            print(f"A classe {qual_classe} nao e reconhecida como uma classe jogavel")
    
   
