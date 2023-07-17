#Importando arquivo com todos os itens do jogo
import Itens.itens_main

#pegando itens
def pegando_item(item):
    if item.name in Itens.itens_main.Itens.itens.itens_list_name:
        import inventario.inv
        inventario.inv.inventario_address.append(item)
        inventario.inv.inventario_name.append(item.name)
    else:
        print("Nao ta presente")