#Dados: d4, d6, d20, d8, d12, d10

#Definindo os dados para o rpg
class Dados:
    def __init__(self, lados):
        self.numero = lados

d4 = Dados(4)
d6 = Dados(6)
d8 = Dados(8)
d10 = Dados(10)
d12 = Dados(12)
d20 = Dados(20)

#Criando o personagem
def criando_personagem_principal():
    print("")
#criando classes de personagens
class Classes:
    def __init__(self,name,damage,life,mana,noise,info):
        self.name = name
        self.base_damage = damage
        self.life = life
        self.mana = mana
        self.info = info
        self.noise = noise

#definindo as classes
draconico = Classes("Draconico", 7, 125, 25, 10, "Draconicos sao pessoas que herdaram poderes de seus ancestrais 'Dragoes' e ganharam mais vida e dano basico porem tambem perderam um pouco de sua mana e sao seres muito barulhentos.")
elfo = Classes("Elfo", 4.5, 80, 75, 2, "Elfos sao seres pequenos que receberam a bencao da floresta o que lhes deu alto nivel de mana e a habilidade de nao fazer muito barulho, mas por se tratarem de seres pequenos, sua vida e dano tiveram uma reducao.")
feral = Classes("Feral", 8.5, 145, 0, 10, "Ferais sao seres descendentes dos felinos que herdaram o dano e a vida de seus ancestrais, mas tambem perderam o poder de usar poder magico")
mago = Classes("Mago", 5, 100, 100, 4, "Magos sao humanos que receberam habilidades atravez de seus conhecimentos especiais. Magos recebem vida de humano e dano de humano porem ganham mana extra")
#colocando as classes em uma lista
classes = [draconico,elfo,feral,mago]

#definindo os personagens padroes
class Characters:
    def __init__(self, name,mana):
        self.name = name
        self.life = None #Tenho que mudar
        self.armor = "x"
        self.mana = mana

#definindo o personagem principal
class main_character(Characters):
    def __init__(self, name, life,mana):
        super().__init__(name, life)
        self.inventory = None
        self.saciedade = 100
        self.mana = mana

#definindo os todos os itens presentes no rpg
class itens:
    def __init__(self, name, damage, noise):
        self.name = name
        self.damage = damage
        self.noise = noise

#definindo espadas que sao derivadas dos itens
class swords(itens):
    def __init__(self, name, damage, noise):
        super().__init__(name, damage, noise)
        pass

#definindo comidas que sao derivadas dos itens
class food(itens):
    def __init__(self, name, damage, noise,saciedade,feeling,energy,mana):
        super().__init__(name, damage, noise)
        self.saciedade = saciedade
        self.feeling = feeling
        self.energy = energy
        self.mana = mana

#definindo comidas
batata = food("batata", 2.5, 2, 7, "Feliz", 3, 0)
banana = food("banana", 0.5, 0, 8, "Normal", 5, 0)

#definindo uma lista dos alimentos
foods = [batata, banana]

#criando o personagem principal
Danielle = main_character("Danielle Maglhaes dos Santos",None,0)

#criando personagens

#criando funcao para comer
def eating():
    what_to_eat = str(input("O que voce gostaria de comer? "))
    for food in foods:
        if food.name == what_to_eat:
            print(food.name)
            Danielle.saciedade += food.saciedade
            print(Danielle.saciedade)

#criando funcao para atacar

#criando funcao para receber acoes
def getting_action():
    action = str(input("O que gostaria de fazer? ")).lower().strip()
    if action == "comer":
        eating()

def introducao():
    print("Apos ter ido em uma festa e ter virado a noite com seus amigos, voce acorda em uma sala branca com uma mulher que aparenta ser um anjo.\n'Vejo que finalmente acordou' Exclamou a mulher.")
    resposta_1 = str(input("Voce decide perguntar:\n(1)Onde estou?\n(2)O que aconteceu?\n(3)Quem é você?"))
    if resposta_1 == "1":
        print("Você está em uma sala onde terais apenas duas opções: 'viver' ou 'morrer'\nSem entender a situacao você a pergunta 'O que aconteceu?'")
        print("Enquanto você voltava para casa, seus amigos te desafiaram a dançar no meio da rua, porem no mesmo momento em que você comecou a dancar, uma abelha te picou e voce morreu devido a sua alergia.")
        print("Com muita decepcao por ter morrido de forma tao estupida voce a pergunta o porque de estar nesta sala sendo que voce ja teria morrido.\n(A Anja:) Você está aqui para nos ajudar a terminar uma guerra antes que seja tarde demais.\n (Anja:) Neste exato momento em um dos mundos que estao sob o meu controle, dois reinos decidiram comecar uma guerra em busca de 5 fragmentos que quando juntos eles se tornam um livro que caso caia em maos erradas podera ser o fim deste mundo.")
        resposta_2 = str(input("Confuso sobre tudo que a 'Anja' falava, voce decide perguntar:\n(1)O que aconteceria se eu recusase a oferta?\n(2)Por que eu?\n(3)Como eu seria capaz de recuperar o livro e enfrentar dois reinos de outro mundo?\n(3)Por que eu aceitaria a oferta?"))
        if resposta_2 == "1":
            print("(Anja:) Você iria para o purgatorio onde irão definir se irá para o céu ou para o submundo")
            resposta_3 = str(input("(Anja:) Caso você aceite a oferta você podera decidir como ira renascer e tera direito de escolher um de três bencaos para te acompanhar durante sua jornada.\n(Narrador:) enteressado na oferta você responde:\n(1)Eu aceito a oferta!\n(2)"))
    elif resposta_1 == "2":
        print("(Anja:) Enquanto você voltava para casa, seus amigos te desafiaram a dançar no meio da rua, porem no mesmo momento em que você comecou a dancar, uma abelha te picou e voce morreu devido a sua alergia.")
        print("(Narrador:) Com muita decepcao por ter morrido de forma tao estupida voce a pergunta o porque de estar nesta sala sendo que voce ja teria morrido.\n(Anja:) Você está aqui para nos ajudar a terminar uma guerra antes que seja tarde demais.\n (Anja:) Neste exato momento em um dos mundos que estao sob o meu controle, dois reinos decidiram comecar uma guerra em busca de 5 fragmentos que quando juntos eles se tornam um livro que caso caia em maos erradas podera ser o fim deste mundo.")
#comecando o jogo
if __name__ == "__main__":
    introducao()