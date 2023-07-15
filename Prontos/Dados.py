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

#Iniciando o codigo
if __name__ == "__main__":
    definindo_dado()