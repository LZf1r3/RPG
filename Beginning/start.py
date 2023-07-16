def acao_2_pergunta():
    pergunta1_list = ["1","Onde estou"]
    pergunta2_list = ["2",""]

    acao_2 = str(input("Voce se aproxima da Anja porem mesmo com medo decide perguntar:\n(1)Onde Estou?\n(2)Quem é você?\n(3)O que aconteceu?"))
    
def acao_2_acao():
    acao_2 = str(input("Sem pensar muito e sem ter muitas opcoes voce opita por:\n(1)Se fingir de morto\n(2)Atacar a Anja\n(3)Fugir correndo\n.:"))

acao_1 = str(input("(Narrador:) Voce aparece me uma sala branca sentindo uma forte dor ardente em seu pescoco. Logo em sua frente voce observa a silhueta de uma pessoa, porem com asas. Ao se aproximar voce percebe que se trada de uma anja. Confuso com a situacao voce decide:\n(1)Fazer Perguntar\n(2)Fazer Ação\n.:")).lower()
if acao_1 == "1" or acao_1 == "fazer pergunta"  or acao_1 == "perguntar" or acao_1 =="pergunta":
    acao_2_pergunta()
elif acao_1 == "2"or acao_1 == "fazer acao" or acao_1 == "acao":
    acao_2_acao()