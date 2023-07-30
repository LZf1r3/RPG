
#Definindo as classe jogaveis tipo (Mago, Elfo, etc...)
class Classes:
    def __init__(self, name, damage, life, mana, noise, info, ataques):
        self.name = name #O nome da classe
        self.base_damage = damage #O dano base da classe sem nenhuma arma (No soco)
        self.life = life #A vida da classe
        self.mana = mana #A mana da classe
        self.info = info #A informacao em txt da classe
        self.noise = noise #O barulho da classe
        self.ataques = ataques #Os ataques personalizados da classe

#!!!!!Funcao criada sem utilizacao / OBS.:(Verificar utilidade da funcao antes de exclui-la)
    #def information(classe_name):
        #classes = [draconico,elfo,feral,mago]
        #for classe in classes:
            #if classe.name == classe_name:
                #print(classe.info)

#Definindo as variaveis do personagem principal
class Main_character_class():
    def __init__(self, classe,vida, dano, mana, saturacao, armadura, armadura_mana,estamina,barulho):
        self.nome = str(input("Como voce gostaria de se chamar neste novo mundo? ")) #Nome com input apos selecionar classe
        self.classe = classe #Definido com funcao no comeco da execucao
        self.vida = vida #Vida definida de acordo com a classe escolhida
        self.dano = dano #Dano definido de acordo com a calsse escolhida
        self.mana = mana #Mana definida de acordo com a classe escolhida
        self.saturacao = saturacao #Saturacao definida de acordo com a classe escolhida
        self.armadura = armadura #Nao esta em execucao ainda
        self.armadura_mana = armadura_mana #Nao esta em execucao ainda
        self.inventario = [] #Nao esta em execucao ainda
        self.level = 1 #Melhorar funcao de ganhar nivel
        self.estamina = estamina #Estamida definida de acordo com a classe escolhida
        self.barulho = barulho #Barulho definido de acordo com a calsse escolhida
        self.ataques = []

    @property
    def escolhendo_ataque(self):
        for numero, ataque in enumerate(self.classe.ataques, start=1):
            print(f"{numero}. {ataque.nome}")
        ataque_escolhido = None
        loop = 0
        while loop != 3:
            try:
                ataque_escolhido = int(input("Digite o numero do ataque: "))
                if self.classe.ataques[ataque_escolhido-1] in self.ataques:
                    print('Voce ja selecionou este ataque. Tente selecionar outro')
                    ataque_escolhido = None
                if ataque_escolhido not in range(1, len(self.classe.ataques)+1):
                    print("Numero de ataque invalido! Tente novamente.")
                    ataque_escolhido = 0
                else:
                    self.ataques.append(self.classe.ataques[ataque_escolhido-1])
                    loop += 1
                    ataque_escolhido = None
            except ValueError:
                print("Ataque nao encontrado! Tente novamente.")
                ataque_escolhido = None
        for numero, ataque in enumerate(self.ataques, start=1):
            print(f"{numero}. {ataque.nome}")

    #Funcao de atacar inimigos
    def atacar(self,weapon,inimigo): #Recebe variavel de armas(espadas, arcos, etc...) e variavel de inimigo
        for ataque in weapon.ataques:
            self.ataques.append(ataque)
        print(f"Voce encontrou um '{inimigo.nome}' level:{inimigo.level}") #Imprimindo informacao do inimigo
        while self.vida >=0 and inimigo.vida >=0: #Criando loop de batalha
            print("Qual ataque voce gostaria de fazer?")
            for ataque in self.ataques:#Loop imprimindo os ataques da arma (!!!Preciso adicionar os ataques da classe tbm!!!)
                print(f"\n{ataque.nome}\nDano:{ataque.dano} Estamina:{ataque.estamina} Mana:{ataque.mana}")#Imprimindo informacoes do ataque
            qual_ataque = str(input(".:"))#Escolhendo ataque
            for ataque in self.ataques: #Loop para verificacao de ataque na lista de ataques da arma selecionada
                if qual_ataque == ataque.nome: #Verificando se o nome dado pelo player bate com o nome dado pela variavel de ataque
                    print(f"Ataque selecionado: {qual_ataque}") #Imprimi o ataque selecionado 
                    if self.estamina < ataque.estamina: #Verificando se o personagem possui estamina 
                        print(f"Voce nao possui estamina suficiente para usar o ataque: {ataque.nome}") #Informando o player que ele nao possui estamina para usar o ataque selecionado
                    elif self.mana < ataque.mana: #Verificando se o personagem possui mana
                        print(f"Voce nao possui mana suficiente para usar o ataque: {ataque.nome}") #Informando o player que ele nao possui mana para usar o ataque selecionado
                    else:
######!!! Resolver problema de vantagens de niveis: !!!######
                        if self.level >= inimigo.level:
                            import Dados_file
                            if self.level >= inimigo.level + 20:
                                dados = Dados_file.D20
                            elif self.level >= inimigo.level + 15:
                                dados = Dados_file.D10
                            elif self.level >= inimigo.level + 10:
                                dados = Dados_file.D8
                            elif self.level >= inimigo.level + 5:
                                dados = Dados_file.D4
                            else:
                                dados = Dados_file.D0
                            bad_dados = Dados_file.D0
                            print(f"Voce possui a vantagem de um {dados.name}\n")
                        
                        elif self.level <= inimigo.level:
                            import Dados_file
                            if inimigo.level >= self.level + 20:
                                bad_dados = Dados_file.D20
                            elif inimigo.level >= self.level + 15:
                                bad_dados = Dados_file.D10
                            elif inimigo.level >= self.level + 10:
                                bad_dados = Dados_file.D8
                            elif inimigo.level >= self.level + 5:
                                bad_dados = Dados_file.D4
                            else:
                                bad_dados = Dados_file.D0
                            dados = Dados_file.D0
                            print(f"Voce possui a desvantagem de um {dados.name}\n")
                        elif self.level == inimigo.level:
                            import Dados_file
                            dados = Dados_file.D0
                            bad_dados = Dados_file.D0
                            print("Voce nao possui vantagem e nem desvantagem\n")
###### Resolver problema de niveis acima

                        inimigo.vida -= (ataque.dano + dados.resultado) #Executando calculo de vida do inimigo apos ataque do player(Tentar colocar em funcao para ficar mais dinamico e organizado)
                        self.vida -= (inimigo.dano + bad_dados.resultado)  #Executando calculo de vida do player apos ataque do inimigo(Tentar colocar em funcao para ficar mais dinamico e organizado)
                        self.estamina -= ataque.estamina #Subtraindo a estamina do player com o valor da estamina do ataque
                        self.mana -= ataque.mana #Subtraindo a estamina do player com o valor da estamina do ataque
                        print(f"Voce causou {ataque.dano+dados.resultado} de dano deixando o inimigo '{inimigo.nome}' com '{inimigo.vida}' de vida. Vida-Restante:{inimigo.vida}") #Imprimindo o dano causado ao inimigo
                        print(f"O jogador '{self.nome}' sofreu um dado de {inimigo.dano+bad_dados.resultado}. Vida-Restante:{self.vida}") #Imprimindo o dano causado ao player
                        print(f"O jogador '{self.nome}' tem {self.estamina} pontos de estamina restante") #Imprimindo a estamina restante do player
                        
                        #IF statement para dizer se o player morreu ou matou o inimigo apos a batalha
                        if self.vida <= 0:
                            print("Game Over!")
                            exit()
                        elif inimigo.vida <= 0:
                            print(f"O jogador '{self.nome}' matou o inimigo '{inimigo.nome}'\n")

#Funcao para saber o que o player deseja fazer tipo (atacar, fugir, etc...)
    def o_que_fazer(self,inimigo): #Recebendo a informacao do inimigo
        ######!!! Fazer comentarios urgentemente !!!######
        oqf = str(input("O que deseja fazer?\n (1)Atacar (2)Fugir (3)Tentar passar sorrateiramente\n.:")).strip().title()
        if oqf == "1" or oqf == "Atacar":
            print("Voce decidiu atacar")
            self.atacar(self.dano,inimigo)
        elif oqf ==  "2" or oqf == "Fugir":
            import Dados_file as dado
            if dado.D20.resultado >= 12:
                print(dado.D20.resultado)
                print("Voce conseguiu fugir")
            else:
                print("Voce nao conseguiu fugir")
                self.atacar(self.dano, inimigo)
        elif oqf == "3" or oqf == "Tentar Passar Sorrateiramente":
            print("Voce decidiu passar na surdina")
            if inimigo.percepcao >= (self.barulho + ((inimigo.percepcao/3)*2)):
                print("Voce consegue fugir por um triz")
            else:
                print("Voce nao consegue fugir pois fez muito barulho!")
                self.atacar(self.dano,inimigo)


#Definindo classe dos inimigos
class inimigos():
    def __init__(self, nome, vida, dano,level,percepcao):
        self.nome = nome #Nome do inimigo
        self.vida = vida #Vida do inimigo
        self.dano = dano #Dano do inimigo
        self.level = level #Level do inimigo
        self.percepcao = percepcao #Percepcao do inimigo (Ficou confuso na parte dos buffs de ataque [Utilizar porcentagem para fazer calculo do buff tipo: {ataque.dano + 20% = ataque.dano + ataque.dano * 0.2}])

    #funcao de atacar
    #Funcao fora de uso porem a mto interessante de fazer para simplificar (tentar usar esta funcao)
    def atacar(self, alvo): #Recebendo o elemento alvo (No caso o player)
        alvo.vida -= self.dano #Atacando o player
        print(f"O inimigo {self.nome} atacou {alvo.nome} e causou {self.dano} pontos de dano!") #Informando o player que ele foi atacado

#Definindo classe de itens
class itens:
    def __init__(self,nome,dano,estamina,mana):
        self.nome = nome #Nome do item
        self.dano = dano #Dano (ficou confuso [Melhor mudar])
        self.estamina = estamina #Estamina que o item gasta
        self.mana = mana #Mana que o item gasta

#Definindo classe de ataques
class ataques:
    def __init__(self,nome,dano,estamina,mana):
        self.nome = nome #Nome do ataque
        self.dano = dano #Dano do ataque
        self.mana = mana #mana que o ataque gasta
        self.estamina = estamina #Estamina que o ataque gasta

#Definindo classe das espadas
class espadas(itens): #Definindo que a classe espada e filha da classe itens
    def __init__(self, nome, dano, estamina, mana, ataques):
        super().__init__(nome, dano, estamina, mana) #Pegando as informacoes de derivacao da classe mae(itens)
        self.ataques = ataques

#Definindo classe para os ataques das espadas
class ataques_espadas(ataques):#Definindo que a classe ataques_espadas e filha da classe ataques
    def __init__(self, nome, dano, estamina, mana):
        super().__init__(nome, dano, estamina, mana)#Pegando as informacoes de derivacao da classe mae(ataques)

#Definindo classe para os ataques das classes
class ataques_de_classe:
    def __init__(self, nome, dano, estamina, mana):
        self.nome = nome
        self.dano = dano
        self.estamina = estamina
        self.mana = mana

#Definindo ataques de espada
estocada_rapida_espada = ataques_espadas("Estocada Rápida", 12, 8, 0)
corte_vertical_espada = ataques_espadas("Corte Vertical", 18, 12, 0)
golpe_frenetico_espada = ataques_espadas("Golpe Frenético", 20, 15, 0)
investida_poderosa_espada = ataques_espadas("Investida Poderosa", 30, 25, 0)
golpe_giratorio_espada = ataques_espadas("Golpe Giratório", 15, 20, 0)
furacao_cortante_espada = ataques_espadas("Furacão Cortante", 22, 18, 0)
estocada_precisa_espada = ataques_espadas("Estocada Precisa", 14, 10, 0)
corte_horizontal_amplo_espada = ataques_espadas("Corte Horizontal Amplo", 20, 16, 0)
golpe_mortal_espada = ataques_espadas("Golpe Mortal", 35, 30, 0)
corte_rapido_espada = ataques_espadas("Corte Rápido", 16, 12, 0)
golpe_fulminante_espada = ataques_espadas("Golpe Fulminante", 40, 35, 0)
investida_impetuosa_espada = ataques_espadas("Investida Impetuosa", 25, 20, 0)
corte_diagonal_espada = ataques_espadas("Corte Diagonal", 18, 15, 0)
estocada_poderosa_espada = ataques_espadas("Estocada Poderosa", 30, 28, 0)
golpe_rapido_espada = ataques_espadas("Golpe Rápido", 14, 12, 0)
corte_investida_espada = ataques_espadas("Corte de Investida", 20, 16, 0)
golpe_furioso_espada = ataques_espadas("Golpe Furioso", 26, 22, 0)
contra_golpe_espada = ataques_espadas("Contra Golpe", 20, 18, 0)
golpe_trovao_espada = ataques_espadas("Golpe Trovão", 35, 30, 0)
estocada_rapida_espada = ataques_espadas("Estocada Rápida", 15, 10, 0)
corte_chamas_espada = ataques_espadas("Corte das Chamas", 28, 22, 0)
golpe_concentrado_espada = ataques_espadas("Golpe Concentrado", 32, 28, 0)
danca_cortante_espada = ataques_espadas("Dança Cortante", 22, 20, 0)
golpe_preciso_espada = ataques_espadas("Golpe Preciso", 20, 18, 0)
investida_frenetica_espada = ataques_espadas("Investida Frenética", 28, 24, 0)
ataque_rapido_espada = ataques_espadas("Ataque Rapido",10,10,0)
golpe_flamejante_espada = ataques_espadas("Golpe Flamejante", 25, 50,0)
danca_das_laminas_espada = ataques_espadas("Dança das Lâminas", 15, 15,0)

# Definindo ataques de classe
# Mago:
bola_de_fogo = ataques_de_classe("Bola de Fogo", 35, 5, 15)
raio_glacial = ataques_de_classe("Raio Glacial", 30, 4, 20)
explosao_arcana = ataques_de_classe("Explosão Arcana", 45, 7, 25)
escudo_de_energia = ataques_de_classe("Escudo de Energia", 0, 10, 20)
metamorfose_elemental = ataques_de_classe("Metamorfose Elemental", 55, 8, 30)
tornado_etereo = ataques_de_classe("Tornado Etéreo", 40, 6, 20)
esfera_sombria = ataques_de_classe("Esfera Sombria", 38, 5, 20)
vortice_do_caos = ataques_de_classe("Vórtice do Caos", 50, 8, 25)
maldicao_profana = ataques_de_classe("Maldição Profana", 30, 4, 15)
invocacao_arcana = ataques_de_classe("Invocação Arcana", 42, 6, 20)
# Elfo:
disparo_de_precisao = ataques_de_classe("Disparo de Precisão", 30, 5, 15)
flecha_flamejante = ataques_de_classe("Flecha Flamejante", 25, 4, 20)
tiro_multiplo = ataques_de_classe("Tiro Múltiplo", 20, 6, 10)
salto_acrobatico = ataques_de_classe("Salto Acrobático", 0, 8, 10)
seta_envenenada = ataques_de_classe("Seta Envenenada", 28, 5, 15)
flecha_de_gelo = ataques_de_classe("Flecha de Gelo", 32, 6, 15)
chuva_de_flechas = ataques_de_classe("Chuva de Flechas", 15, 10, 25)
flecha_perfurante = ataques_de_classe("Flecha Perfurante", 35, 7, 18)
sopro_da_natureza = ataques_de_classe("Sopro da Natureza", 40, 7, 20)
evasao_elfica = ataques_de_classe("Evasão Élfica", 0, 12, 15)
# Feral
Investida_Brutal = ataques_de_classe("Investida Brutal", 40, 12, 0)
Garras_Sombrias = ataques_de_classe("Garras Sombrias", 35, 8, 0)
Furia_Desenfreada = ataques_de_classe("Fúria Desenfreada", 50, 15, 0)
Roar_Aterronizante = ataques_de_classe("Roar Aterrorizante", 0, 10, 0)
Corte_Giratorio = ataques_de_classe("Corte Giratório", 38, 10, 0)
Berserker = ataques_de_classe("Berserker", 45, 14, 0)
Salto_Predatorio = ataques_de_classe("Salto Predatório", 30, 8, 0)
Mordida_Voraz = ataques_de_classe("Mordida Voraz", 32, 9, 0)
Finta_Mortal = ataques_de_classe("Finta Mortal", 42, 11, 0)
Forma_Bestial = ataques_de_classe("Forma Bestial", 0, 20, 0)
# Draconico
##Add info about the class draconic

# Criando listas com os ataques de cada classe
ataques_mago = [bola_de_fogo, raio_glacial, explosao_arcana, escudo_de_energia, metamorfose_elemental, tornado_etereo, esfera_sombria, vortice_do_caos, maldicao_profana, invocacao_arcana]
ataques_elfo = [disparo_de_precisao, flecha_flamejante, tiro_multiplo, salto_acrobatico, seta_envenenada, flecha_de_gelo, chuva_de_flechas, flecha_perfurante, sopro_da_natureza, evasao_elfica]
ataques_feral = [Investida_Brutal, Garras_Sombrias, Furia_Desenfreada, Roar_Aterronizante, Corte_Giratorio, Berserker, Salto_Predatorio, Mordida_Voraz, Finta_Mortal, Forma_Bestial]


#Criando variaveis de leitura do arquivo txt das classes onde tem a informacao necessaria delas
drac_file = open("RPG/Classes_info_folder/Draconico.txt","r") #Variavel das informacoes detalhadas da classe draconico
elfo_file = open("RPG/Classes_info_folder/Elfo.txt","r") #Variavel das informacoes detalhadas da classe elfo
fera_file = open("RPG/Classes_info_folder/Feral.txt","r") #Variavel das informacoes detalhadas da classe feral
mago_file = open("RPG/Classes_info_folder/Mago.txt","r") #Variavel das informacoes detalhadas da classe mago

#Definindo as classes
draconico = Classes("Draconico", 7, 125, 25, 10,drac_file.read(),[]) #Definindo classe Draconico
elfo = Classes("Elfo", 4.5, 80, 75, 2, elfo_file.read(),[disparo_de_precisao,flecha_flamejante,tiro_multiplo,salto_acrobatico,seta_envenenada,flecha_de_gelo,chuva_de_flechas,flecha_perfurante,sopro_da_natureza,evasao_elfica]) #Definindo classe elfo
feral = Classes("Feral", 8.5, 145, 0, 10, fera_file.read(),[Investida_Brutal, Garras_Sombrias, Furia_Desenfreada, Roar_Aterronizante, Corte_Giratorio, Berserker, Salto_Predatorio, Mordida_Voraz, Finta_Mortal, Forma_Bestial]) #Definindo classe feral
mago = Classes("Mago", 5, 100, 100, 4, mago_file.read(),[bola_de_fogo, raio_glacial, explosao_arcana, escudo_de_energia, metamorfose_elemental, tornado_etereo, esfera_sombria, vortice_do_caos, maldicao_profana, invocacao_arcana]) #Definindo classe mago

#Criando lista das classes que e mto importante 
num_classes = [draconico,elfo,feral,mago]#Lista das classes

#Definindo inimigos
#Comentar dps (Nao e de extrema importancia)
lvl_1 = inimigos("Gordon", 50, 4, 1, 0)
lvl_2 = inimigos("Goblin", 75, 5, 2, 2)
lvl_3 = inimigos("Goblin Verde", 100, 6, 3, 2)
lvl_4 = inimigos("Goblin Vermelho", 115, 8, 4, 2.5)
lvl_5 = inimigos("Gordon Remastered", 125, 10, 5, 5)
lvl_6 = inimigos("Cobra", 150, 10, 6, 5.5)
lvl_7 = inimigos("Guarda Goblin", 200, 15, 7, 8)
lvl_8 = inimigos("Goblin de Elite", 225, 20, 8, 9)
lvl_9 = inimigos("Vice Rei Goblin", 250, 25, 9, 9.5)
lvl_10 = inimigos("Gordon the Goblin GOD", 500, 50, 10, 10)

#Funcao de ajuda que sera utilizada no comeco do codigo
def help():
    for classe in num_classes: #(Loop and Print) -> para informar as informacoes basicas de cada classe presente na lista de classes
        print(f"\nInformacoes da classe {classe.name}\nNome:{classe.name}\nVida:{classe.life}\nMana:{classe.mana}\nDano-Base:{classe.base_damage}\nBarulho:{classe.noise}\nAtaques:")
        for numero, ataque in enumerate(classe.ataques, start=1):
            print(f"    {numero}. {ataque.nome}")
        print("---------------------------//---------------------------")
    qual_classe = str(input("Digite 'continue' caso deseije selecionar alguma classe ou digite o nome da classe para descobrir mais sobre ela: ")).title().strip()#Perguntando para o player qual a classe ele quer informacoes detalhadas ou se ele nao precisa mais delas
    #IF statement que define se o usuario vai seguir para escolher a classe ou se ele que saber a informacao de alguma classe
    if qual_classe == "Continue":
        pass
    else:
        for classe in num_classes:#Loop que seleciona a classe para ser verificada
            if qual_classe == classe.name:#Verificando se o nome dado pelo player bate com o nome dado na variavel
                print(f"Informacoes sobre a classe: '{classe.name}':\n{classe.info}")#Imprimindo as informacoes detalhadas da classe selecionada
        with open("RPG/Playable_classes.txt","r") as file: #Abrindo arquivo das classes jogaveis
            if f"{qual_classe}\n" not in file.readlines(): #verificando se o nome dado pelo player nao esta no arquivo de classes jogaveis
                print("Classe nao encontrada! Tente novamente.") #imprimindo que o a classe dada pelo player nao e jogavel
                help() #Executando a funcao help denovo


setado = None
while setado != 0:
    try:
        qual_classe = str(input("Digite o nome da classe ou digite 'help' para saber as informacoes sobre uma determinada classe.\n.:")).strip().title()
        if qual_classe == "@Adm":
            print("Entrando em modo adm...")
            break
        with open("RPG/Playable_classes.txt","r") as file:
            if qual_classe == "Help":
                help()
                setado = None
            elif f"{qual_classe}\n" not in file.readlines():
                print(f"A classe {qual_classe} nao e reconhecida como uma classe jogavel! Tente novamente.")
                setado = None
            else:
                with open("RPG/Playable_classes.txt","r") as file:
                    for line in file.readlines():
                            if f"{qual_classe}\n" == line:
                                for classe in num_classes:
                                    if qual_classe == classe.name:
                                        player = Main_character_class(classe,classe.life,classe.base_damage,classe.mana,0,2,3,100,classe.noise)
                                        print(f"\nPlayer:{player.nome}\nClasse:{player.classe.name}\nVida:{player.vida}\nEstamina:{player.estamina}\nDano:{player.dano}\nMana:{player.mana}\nSaturacao:{player.saturacao}\nArmadura-mana:{player.armadura_mana}\nArmadura-defesa:{player.armadura}\n\n")
                                        setado=0
    except ValueError:
        print("Tente novamente.")
#Funcao de escrever classes em um txt
def writing_classes():
        for classe in num_classes:
            with open("RPG/Playable_classes.txt","r") as file_r:
                if f"{classe.name}\n" in file_r.readlines():
                    print(f"A classe {classe.name} ja esta salva!")
                else:
                     with open("RPG/Playable_classes.txt","a") as file_w:
                          file_w.write(f"{classe.name}\n")

ouro = espadas("Espada de ouro", 1, 1, 1, [golpe_flamejante_espada, ataque_rapido_espada])
player.escolhendo_ataque
player.atacar(ouro,lvl_2)
print("\n\n♡ ♡ ♡\n\n")