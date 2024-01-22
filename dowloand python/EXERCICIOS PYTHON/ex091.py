from random import randint 
from time import sleep
from operator import itemgetter #Essa função me permite pegar somente o "indice" que eeu quero num dicionario, podendo manipula-lo como se fosse uma lista 
jogador = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = {}
for k,v in jogador.items():
    print (f'{k} tirou {v} no dado')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse = True)#DEesa maneira eu manipulo somente o valor do meu indice, que basicamnete corresponde ao um indice 1. sendo assim, ponho em ordem com base no valor. 
print ('-='*30)
print ('{:^30}'.format('== RANKING DOS JOGADORES =='))
for i, v in enumerate(ranking):
    print (f'{i+1}º lugar: {v [0]} com {v[1]}')#O itemgetter realmente me permite manipular os indices e valores do dicionário como se fossem em listas, trasnformando-os em números

'''cont = 1
for k, v in (ranking):
    print(f'{cont}º lugar: {k} com {v}. ')
    cont += 1.''' #Outra forma de ser feito