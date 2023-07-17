#imporatndo random para ser o dado
import random

#Classe dos dados utilizados no Rpg
class Dados:
    def __init__(self, numero_de_lados, nome):
        self.lados = numero_de_lados
        self.name = nome
        self.buff = 0
        
    #Rodando os numeros dos dados
    @property
    def rodando_dados(self):
        dado_func = random.randint(self.buff if self.buff >= 1 else 1 ,self.lados)
        print(f"{self.name}: {dado_func}")
        
#Definindo os valores e os dados existentes
D4 = Dados(4,"D4")
D6 = Dados(6,"D6")
D8 = Dados(8,"D8")
D10 = Dados(10,"D10")
D12 = Dados(12,"D12")
D20 = Dados(20,"D20")

#Enlistando os dados
dados = [D4,D6,D8,D10,D12,D20]

#Definindo qual dado
def definindo_dado():
    tipo_dado = str(input("Qual o tipo de dado?\n")).capitalize().strip()
    #loop para verificar qual o dado que foi selecionado
    for dado in dados:
        if dado.name == tipo_dado: 
            dado.rodando_dados

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

    def atacar(self,espada,player,inimigo):
        while player.vida >=0 and inimigo.vida >=0:
            print("Qual ataque voce gostaria de fazer? ")
            for ataque in espada_de_ouro.ataques:
                print(ataque.nome)
            qual_ataque = str(input(".:"))
            for ataque in espada_de_ouro.ataques:
                if qual_ataque == ataque.nome:
                    inimigo.vida = inimigo.vida - (ataque.dano - D4.rodando_dados)
                    print(f"A vida do inimigo e:{inimigo.vida}")
                else:
                    pass

class inimigos():
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self, alvo):
        alvo.vida -= self.dano
        print(f"O inimigo {self.nome} atacou {alvo.nome} e causou {self.dano} pontos de dano!")


qual_classe = str(input("Digite o nome da classe ou digite 'help' para saber as informacoes sobre uma determinada classe.\n")).strip().title()
with open("Rpg_finalizado/Playable_classes.txt","r") as file:
    for line in file.readlines():
            if f"{qual_classe}\n" == line:
                for classe in num_classes:
                    if qual_classe == classe.name:
                        player = Main_character_class(qual_classe,classe.life,classe.base_damage,classe.mana,0,2,3)
                        print(f"Player:{player.nome}\nClasse:{player.classe}\nVida:{player.vida}\nDano:{player.dano}\nMana:{player.mana}\nSaturacao:{player.saturacao}\nArmadura-mana:{player.armadura_mana}\nArmadura-defesa:{player.armadura}")
                    else:
                        pass
            else:
                pass
    
   #################################################################################

class espadas:
    def __init__(self,nome,dano,ataques):
        self.nome = nome
        self.dano = dano
        self.ataques = ataques
    
    def atacar(self,player,inimigo):
        print("Qual ataque voce deseja executar?")
        for ataque in self.ataques:
            print(ataque.nome)

class ataques_espadas:
    def __init__(self,nome,dano,estamina):
        self.nome = nome
        self.dano = dano
        self.estamina = estamina

ataque_rapido_espada = ataques_espadas("Ataque Rapido",10,10)
golpe_flamejante_espada = ataques_espadas("Golpe Flamejante", 30, 50)
danca_das_laminas_espada = ataques_espadas("Dança das Lâminas", 15, 15)

espada_de_ouro = espadas("Espada_de_ouro",5,[ataque_rapido_espada,golpe_flamejante_espada,danca_das_laminas_espada])
inimigo = inimigos("Goblin", 50, 10)
player.atacar(espada_de_ouro,player,inimigo)