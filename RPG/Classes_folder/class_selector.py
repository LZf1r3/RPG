print("Please choose one of the following races to be reborn with: ")
#Importando as classes
import Classes_folder.Classes as Classes
import Personagens.Main_character as pr

#definindo loop de impressao das classes no terminal
def loop():
    x = 1
    for classe in Classes.num_classes: #importando lista das classes para o loop de for
        print(f"{x}. {classe.name}")
        x+=1

#Escolhendo a classe de jogo / OBS.:(Error no final que esta sendo resolvido no arquivo Classes.py onde estou tendando escrever o nome das classes em um txt e depois verificar se ja existe.)
def escolhendo_classe():
    qual_classe = str(input("Digite o nome da classe ou digite 'help' para saber as informacoes sobre uma determinada classe.\n")).strip().title()
    if qual_classe == "Help":
        help(qual_classe)
    elif qual_classe == Classes.elfo.name:
        Elfo()
    elif qual_classe == Classes.mago.name:
        Mago()
    elif qual_classe == Classes.feral.name:
        Feral()
    elif qual_classe == Classes.draconico.name:
        Draconico()
    else:
        with open("RPG/Classes_folder\Playable_classes.txt","r") as file_r:
            if f"{qual_classe}\n" not in file_r.readlines():
                print(f"A classe {qual_classe} nao e recognizada como uma classe jogavel. Por favor acessar menu help.")
                escolhendo_classe()
            else:
                print('Error with statement')

#Definindo as classes de acordo com a escolha do protagonista
def Elfo():
    print("Classe Selecionada: Elfo")
    pr.Main_character(Classes.elfo)

def Mago():
    print("Classe Selecionada: Mago")
    pr.Main_character(Classes.mago)

def Draconico():
    print("Classe Selecionada: Draconico")
    pr.Main_character(Classes.draconico)

def Feral():
    print("Classe Selecionada: Feral")
    pr.Main_character(Classes.feral)

#Funcao para imprimir informacoes sobre as classes
def help(qual_classe):
    print("Qual classe deseja saber as informacoes?")
    loop()
    qual_classe = str(input(":")).title().strip()
    with open("RPG/Classes_folder/Playable_classes.txt","r") as file:
        if f"{qual_classe}\n" in file.readlines():
            for classe in Classes.num_classes:
                if classe.name == qual_classe:
                    print(classe.info)
                    escolhendo_classe()
        else:
            print(f"The class {qual_classe} is not recognized as a playable class! Please try again")
            escolhendo_classe()

escolhendo_classe()