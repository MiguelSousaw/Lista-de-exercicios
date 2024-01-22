from random import randint
from time import sleep
def sorteio (lista):
    print('Sorteando 5 valores da lista: ', end = '')
    for contador in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end = '', flush = True)
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}') 

#programa principal= []
numeros = list()
sorteio(numeros)
somapar(numeros)