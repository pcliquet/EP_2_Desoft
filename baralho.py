import random
# def cria_baralho():
#     naipe = random('♠','♥','♦','♣')
#     carta =str(random.randint(1,13))
#     lis = []
#     while i <=52:
#         lis.append(carta+naipe)
#         i+=1
#     return lis
#card = random.randint(1,13)
naipe = random.choices('♠♥♦♣')

print(naipe)