from random import randint
from time import sleep 
print ('-'*40)
print ('{:^40}'.format('JOGA NA MEGA SENA'))
print ('-'*40)
lista = []
jogos = []
tot = 1
quant = int(input('Quantos jogos você quer fazer? '))
while tot <= quant: 
    cont = 0
    while True: 
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()  
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print ('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print (f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)

# A TECNICA USADA NESTE PROGRAMA BASICAMENTE COPIA UMA LISTA ENORME PARA DENTRO DE OUTRA LISTA COPIADA, DENTRO DESSA LISTA COPIADA, A TRANSFORMAMOS EM UMA LISTA COMPOSTA, DE 6 INDICES CADA LISTA MENOR, DEPOIS DISSO, PEDIMOS QUE O PROGRAMA NOS MOSTRE POR INDICES DE ACORDO COM A QUANTIDADE DE JOGOS QUE O USUÁRIO NOS PEDIR, SE O USUÁRIO NOS PEDE 30 JOGOS POR EXEMPLO: O PROGRAMA IRÁ MOSTRAR UMA QUANTIDADE DE 30x6 NÚMEROS DIVIDIDOS EM 30 INDICES DE 6 SUB-INDICES CADA.
