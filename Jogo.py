escolha = input("Deseja jogar este jogo? (Sim/Não): ")
if escolha == "Sim":
    print ("Bem vindo à floresta!")
else:
  print("OK, o jogo não foi iniciado")
  exit ()
introducao = ("Bem-vindo a floresta encantada, você, um corajoso aventureiro, armadilhas traiçoeiras testam sua coragem a cada passo. Prepare-se a Floresta das Sombras guarda segredos que podem levar à glória")
print (introducao)
escolha1 = input("\nQueres ir para a direita ou esquerda? (direita/esquerda): ")
if escolha1 == "direita":
    print("Boa conseguiste passar a entrada da floresta!")
else:
    print("\nUma armadilha apanhou-te e vais ter que voltar para tras!")
    exit()
umparte = ("Passaste a primeira parte da floresta, tens aqui uma faca que te pode ajudar!")
print (umparte)
escolha2 = input("\nQueres ir para a direita ou esquerda? (direita/esquerda: ") 
if escolha2 == "direita":
    print("Fizeste uma má escolha e vais ter que voltar para tras!")
    exit()   
else:
    print("\nFizeste uma boa escolha e podes continuar tem cuidado com cada passo que dás!") 
           
doisparte = ("\nPassaste as duas primeiras partes da floresta,cuidado com as tuas escolhas alguma delas pode ser traiçõeira.")
print(doisparte)   
escolha3 = input("\n Agora tu vais ter de escolher entre uma lanterna para te ajudar no caminho ou um remedio caso te aconteça alguma coisa (medicamento/lanterna): ")

if escolha3 == "medicamento":
    print("\nBoa escolha agora tens um remedio e uma faca na tua mochila caso algum monstro te ataque")
        
else:     
    print("Boa escolha agora tens uma lanterna e uma faca na tua mochila caso algum monstro te ataque ")

tresparte = ("\nPassaste a terceira parte da floresta, cuidado!")    
print(tresparte)    
escolha4 = input("\nOuvi dizer que há um monstro aqui, podes escolher entre tentar lutar contra ele e teres comida ou podes ir para a esquerda e tentar passar pelo caminho mais seguro(tentar/es)")
if escolha4 == "tentar":    
    print("Tens sorte em ter encontrado um animal pequeno, mesmo assim ele feriu-te não te esqueças que tens um remédio na tua mochila, tenta tirar os alimentos que conseguires e coloca-os na tua mochila.")
else:
    print("Boa escolha, tens um caminho seguro e podes continuar, mas não te esqueças que mesmo sendo um caminho seguro podes ter azar!")

escolha5 = input("\nOuvi dizer que há uma caberna por aqui, podes escolher entre entrar ou seguir o teu caminho(entrar/cagão): ")
if escolha5 == "entrar":
    print("Boa escolha, vai entrando na caberna com cautela!")
else:
    print("Escolha boa mas és um cagão, perdeste uma caixa surpresa e ainda ficaste preso numa armadilha.")
    exit()

escolha6 = input("\nA caberna tem 2 caixas lá dentro, podes escolher entre a preta ou a vermehla(preta/vermelha): ")
if escolha6 == "preta":
    print("Boa que ganda sorte mano encontraste uma espada, um casaco de frio e alguma comida!")
else:
    print("Que porcaria que escolheste, não tens sorte nenhuma e a caixa era uma armadilha,  e ficaste preso!")
    exit()
escolha7 = input("\nAgora que tens tudo que precisas para sair da caverna, procura bem que provavelmente vais encontrar uma saida secreta")

escolha8 = input("\nEncontraste a saída, preferes sair da caverna pela passagem secreta ou arriscar e dar a volta por fora.(secreta/volta)")
if escolha8 == "secreta":
    print ("Boa escolha, conseguiste escapar da caverna e da floresta fizeste as boas escolhas, parabéns!")
else:     
    print ("Saiste pela entrada principal da caverna e ficaste preso numa armadilha, perdeste!")
    exit()
