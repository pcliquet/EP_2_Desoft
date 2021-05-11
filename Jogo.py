from baralho import cria_baralho, extrai_naipe, extrai_valor, lista_movimentos_possiveis, empilha
print('')
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

jogar = False
res_1 = input('')
if res_1 == '':
    jogar = True
i = 1

des = 1


#Cria o baralho
baralho = cria_baralho()
naipe = extrai_naipe(baralho[0])
print(naipe)
#Jogo
while jogar == True:
    
    for items in baralho:
        print('{0}.'.format(i), items)
        i+=1
    perg_1 = int(input('escolha uma posição de 1 a {0} '.format(i-1))) -1
    if perg_1 == 100:
        fim = input('voce qure jogar novamente? (sim/nao)')
        if fim =='nao':
            jogar = False

    verifica = lista_movimentos_possiveis(baralho,perg_1) 
    print(verifica)
    if len(verifica) > 1:
        des = int(input('Em qual carta deseja empilhar? \n 1.{0}\n 2.{1}\n'.format(baralho[perg_1 - 1],baralho[perg_1 - 3])))
    baralho = empilha(baralho,perg_1, verifica[des - 1])  



    
    
    i = 1