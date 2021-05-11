import random

def cria_baralho():
    lis = []
    carta = []
    nipe = []
    i=0
    while i<500:
        naipe = random.choices('♠♥♦♣')
        card = str(random.randint(1,13))
        if card == '1':
            card = 'A'
        if card == '11':
            card = 'J'
        if card == '12':
            card ='Q'
        if card == '13':
            card = "K"
        carta = card+naipe[0]
        if carta in lis:
            del(carta)
        else:
            lis.append(carta)
        if len(lis) == 55:
            break
        i+=1
    return lis
baralho = cria_baralho()

#print(baralho)

def extrai_naipe(string):
    tam = len(string)
    return string[tam-1]

def extrai_valor(string):
    tam = len(string)
    res = string[:tam-1]
    return res

def lista_movimentos_possiveis(lista,n):
    i = 0
    poss_1 = False
    poss_2 = False
    mov = []
    naipe_1 = extrai_naipe(lista[n])
    naipe_2 = extrai_naipe(lista[n-1])
    naipe_3 = extrai_naipe(lista[n-3])
    valor_1 = extrai_valor(lista[n])
    valor_2 = extrai_valor(lista[n-1])
    valor_3 = extrai_valor(lista[n-3])
    if n > len(lista):
        return 'Não é possivel movimentar'
    if n == 0 :
        return 'Não é possivel movimentar'
    if naipe_1 == naipe_2 or valor_1 == valor_2:
        poss_1 = True
        mov.append(1)
    if naipe_1 == naipe_3 or valor_1 == valor_3:
        poss_2 = True 
        mov.append(3)
    if poss_1 == True and poss_2 == True:
        return mov, 'Qual carta deseja empilhar \n' '1.{0}\n 2.{0}'.format(lista[n-1],lista[n-3])
    if poss_1 == False and poss_2 == False:
        return 'Não é possivel movimentar'
    if poss_1 == True or poss_2 == True:
        return mov
        



lista = ['6♥', 'J♥', '9♣', '9♥']
def empilha(lista,o,d):
    lista[d] = lista[o]
    del lista[o]
    n_bara = []
    for items in lista:
        n_bara.append(items)
    return n_bara
print(empilha(lista,1,0))


def possui_movimentos_possiveis(lista):
    l = 1
    poss_3 = False
    poss_4 = False
    while l < len(lista)-1:
        naipe_1 = extrai_naipe(lista[l])
        naipe_2 = extrai_naipe(lista[l-1])
        naipe_3 = extrai_naipe(lista[l-3])
        valor_1 = extrai_valor(lista[l])
        valor_2 = extrai_valor(lista[l-1])
        valor_3 = extrai_valor(lista[l-3])
        if l-3 < 0:
            poss_2 = False
        if naipe_1 == naipe_2 or valor_1 == valor_2:
            poss_3 = True
        if naipe_1 == naipe_3 or valor_1 == valor_3:
            poss_4 = True 
        l+=1
    if poss_3 == True or poss_4 == True:
        return True
    else:
        return False