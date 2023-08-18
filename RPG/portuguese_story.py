from time import sleep as sp
def comeco():
    class characters:
        def __init__(self,nome):
            self.nome = nome
    
    nr = characters(f"\n(Narrador): ")
    main = characters(f"\n(You): ")
    ang = characters(f"\n(Anja): ")
    print(f"{nr.nome}Apos festejar a noite toda com seus amigos voce acorda em uma sala branca com uma forte sensacao de queimacao no seu pescoco. Ao observar o seu redor voce observa a silhueta que parecia a de um anjo. Mesmo com medo voce decide ir ate ele e perguntar o que aconteceu.\n")
    print(f"{main.nome}Ola, quem e voce e o porque estou aqui?")
    print(f"{ang.nome}Fico feliz que tenha acordado, espero que esteja bem. Eu me chamo Elina, sou uma anja que controlo 3 mundos sendo um deles o seu.")
    print(f"{nr.nome}Admirado com a beleza e suavidade de sua voz voce simplesmente aceita o que esta acontecendo achando que se passaria por um sonho.")
    ang.nome = f"\n(Elina): "
    print(f"{ang.nome}Ja que esta tao curioso vou te contar o que aconteceu, porem receio que possa ser bem chocante.\n\n{ang.nome}Voce estava festejando a chegada de uma nova estudante na sua sala mas devido ao horario os donos da festa decidiram encerra-la ja que eram quatro horas da manha. No caminho para casa voce e mais tres amigos estavam andando na calcada quando um de seus amigos 'Matheus' te desafiou a dancar no meio da rua. Querendo provar que seria corajoso voce decidiu ir dancar mas quando comecou uma abelha acabou picando o seu pescoco e devido a sua alergia extrema a picadas voce acabou morrendo e vindo parar aqui.")