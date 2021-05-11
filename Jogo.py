from baralho import cria_baralho, extrai_naipe, extrai_valor, lista_movimentos_possiveis, empilha, possui_movimentos_possiveis
#Constantes
i = 1
des = 1
jogar = False
cria_b = False

#Cores
RED   = "\033[1;31m" 
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"
BLUE  = "\033[1;34m"
BOLD    = "\033[;1m"
RESET = "\033[0;0m"
REVERSE = "\033[;7m"
MAGENTA = "\u001b[35m"

print(RESET + '')
print('')
print('')
print('Paciencia Acordeão')
print("==================")
print('')
print('Seja bem-vindo(a) ao jogo Paciência Acordeão!')
print('Seu objetivo é conseguir empilhar todo o baralho respeitando essas condições:')
print('')
print('')
print('')
print('1. As duas cartas possuem o mesmo valor')
print('2. As duas cartas possuem o mesmo naipe')
print('========================================')
print('Você pode empilhar comparando com a ultima carta que você moveu ou com a de dois movimentos anteriores')
print('A carta selecionar ocupará a posição da que você escolheu sobrepor')
print('')
print('')
print('Aperte [ENTER] para começar:')


#inicializa o jogo
res_1 = input('')
if res_1 == '':
    jogar = True
    cria_b = True



#Jogo
while jogar == True:

    #Cria baralho
    if cria_b == True:
        baralho = cria_baralho()
        cria_b = False

    print('Situação atual:')
    print('===============')
    #Layout do Baralho
    for items in baralho:
        if extrai_naipe(items) == '♠':
            print( RESET + '{0}.'.format(i), MAGENTA + items)
        if extrai_naipe(items) == '♥':
            print(RESET + '{0}.'.format(i), RED + items)
        if extrai_naipe(items) == '♦':
            print(RESET + '{0}.'.format(i), GREEN+ items)
        if extrai_naipe(items) == '♣':
            print(RESET + '{0}.'.format(i),BLUE+ items)

        i+=1


    #Movimento do jogador
    while True:
        print(BOLD + 'escolha uma posição de 1 a {0}: '.format(i-1))
        perg_1 = int(input()) -1
        if perg_1 >= len(baralho):
            print('Numero invalido')
        else:
            break    

    verifica = lista_movimentos_possiveis(baralho,perg_1) 
    
    #Verifica o movimento e aplica
    if verifica != 'Não é possivel movimentar':
        if len(verifica) == 1:
            des = verifica[0]
        if len(verifica) != 1:
            des = input('Em qual carta deseja empilhar? \n 1.{0}\n 2.{1}\n'.format(baralho[perg_1 - 1],baralho[perg_1 - 3]))
            if des == '1':
                des = 1
            if des == '2':
                des = 3

        
        #Atualiza o baralho
        print('você empilhou {0} na posição do {1}'.format(baralho[perg_1],baralho[perg_1-des]))
        
        baralho = empilha(baralho,perg_1, perg_1-des) 
        while True:
            perg_3 = input('Quer imprimir o novo baralho? Ou quer analisar assim mesmo? (aperte [Enter] para novo baralho, ou digite algo para repetir a pergunta) ')
            if perg_3 == '':
                break
    if verifica == 'Não é possivel movimentar':
        print( 'Não é possivel movimentar')



    #Verifica se é possivel jogar
    pos = possui_movimentos_possiveis(baralho)
    
    
    # Verifica se o jogador ganhou ou perdeu o jogo
    if pos == False and len(baralho) > 2:
        print('Você Perdeu')
        nova = input('Quer jogar novamente?(sim/nao) ')
        if nova == 'sim':
            jogar = True
            cria_b = True
        else:
            break
    if pos == False and len(baralho) == 1:
        print('Você ganhou')
        nova = input('Quer jogar novamente?(sim/nao) ')
        if nova == 'sim':
            jogar = True
            cria_b = True
        if nova == 'nao':
            jogar = False
    i = 1


