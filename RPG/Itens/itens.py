#Criando classe mae de todas a coisas presentes no rpg
class itens_class:
    def __init__(self, name, damage, noise, tier):
        self.name = name
        self.damage = damage
        self.noise = noise
        self.tier = tier

#criando listas com o endereco do objeto e o nome do mesmo
itens_list_address = []
itens_list_name = []

#Adicionando os objetos nas listas acima
def adicionar_item_address(item):
    if item not in itens_list_address:
          itens_list_address.append(item)
    else:
         print(f"O item {item} ja esta na lista de itens")

#Adicionando o nome dos objetos nas listas acima
def adicionar_item_name(item_name):
    if item_name not in itens_list_name:
          itens_list_name.append(item_name)
    else:
        print(f"O item {item_name} ja esta na lista de itens")

#Escrevendo os itens em um arquivo txt
def writing_itens():
    for item in itens_list_name:
            with open("RPG/Itens/itens.txt","r") as file_r:
                if f"{item}\n" in file_r.readlines():
                    print(f"O item {item} ja esta salvo!")
                else:
                     with open("RPG/Itens/itens.txt","a") as file_w:
                          file_w.write(f"{item}\n")

