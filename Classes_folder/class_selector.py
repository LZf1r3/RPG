print("Please choose one of the following races to be reborn with: ")
#Importando as classes
import Classes

#definindo loop de impressao das classes no terminal
def loop():
    x = 1
    for classe in Classes.num_classes: #importando lista das classes para o loop de for
        print(f"{x}. {classe.name}")
        x+=1

#Escolhendo a classe de jogo / OBS.:(Error no final que esta sendo resolvido no arquivo Classes.py onde estou tendando escrever o nome das classes em um txt e depois verificar se ja existe.)
def escolhendo_classe():
    qual_classe = str(input("Digite o nome da classe ou digite 'help' para saber as informacoes sobre uma determinada classe.\n")).strip().lower()
    if qual_classe == "help":
        print("Qual classe deseja saber as informacoes?")
        loop()
        qual_classe = str(input("?")).title().strip()
        for classe in Classes.num_classes:  #importando lista das classes para o loop de for
            if classe.name == qual_classe:
                print(classe.info)
#Funcao de if que necessita do arquivo Classes.py finalizado para conferir se o nome esta no arquivo txt
        #if qual_classe not in classe.name:
        #    print(f"Error! The classe '{qual_classe}' is not recognized as a playable class")
        #    escolhendo_classe()

loop()
escolhendo_classe()