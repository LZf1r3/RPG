#importacoes
#import Classes_folder.class_selector as cs
#import Itens.armamentos.armaduras as arm

### Arquivo mestre do Rpg inteiro ###

#importando todos os itens do jogo
import Itens.itens_main

#Mandando escrever os itens em um arquivo txt
Itens.itens_main.Itens.itens.writing_itens()

#Importando arquivo de coletar itens
import Acoes.coletando_item

#executando acao de coletar item
Acoes.coletando_item.pegando_item(Itens.itens_main.Itens.armamentos.armaduras.cavalheiro_iniciante)#Cavalheiro_iniciante e o item salvo no diretorio escrito a esquerda do mesmo

#print para comecar o jogo
print("###################################################################################")

#importando e executando a funca de selecionar classe
import Classes_folder.class_selector



