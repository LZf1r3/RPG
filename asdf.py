

class PersonagemPrincipal:
    def __init__(self, nome, vida, dano, mana, saturacao, armadura, armadura_mana):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.mana = mana
        self.saturacao = saturacao
        self.armadura = armadura
        self.armadura_mana = armadura_mana
        self.inventario = []

    def atacar(self, alvo):
        alvo.vida -= self.dano
        print(f"{self.nome} atacou {alvo.nome} e causou {self.dano} de dano!")

    def usar_magia(self, magia, alvo):
        if self.mana >= magia.custo_mana:
            self.mana -= magia.custo_mana
            alvo.vida -= magia.dano
            print(f"{self.nome} usou a magia {magia.nome} em {alvo.nome} e causou {magia.dano} de dano!")
        else:
            print(f"{self.nome} não tem mana suficiente para usar a magia {magia.nome}!")

# Exemplo de criação de um personagem principal
personagem = PersonagemPrincipal("Anja", 100, 20, 50, 100, 10, 5)

# Exemplo de ataque do personagem principal
inimigo = PersonagemPrincipal("Inimigo", 80, 15, 0, 0, 5, 0)
personagem.atacar(inimigo)

# Exemplo de uso de magia pelo personagem principal
class Magia:
    def __init__(self, nome, dano, custo_mana):
        self.nome = nome
        self.dano = dano
        self.custo_mana = custo_mana

magia_fogo = Magia("Bola de Fogo", 30, 20)
personagem.usar_magia(magia_fogo, inimigo)