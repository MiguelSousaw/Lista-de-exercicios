from random import randint
from time import sleep
# Novo Recurso: itens = ('pedra', 'papel', 'tesoura')
#               maquina = randint(0,2)
#              print (itens [computaor])
#função: Transformar a variavel nos itens 

print ('Suas opções: ')
print ('[1] PEDRA')
print ('[2] PAPEL')
print ('[3] TESOURA')
jogada= int(input('Qual é sua jogada?'))
maquina = randint(1,3)
print ('JO')
sleep(1)
print ('KEN')
sleep (1)
print ('PO!!')
sleep (1)

if maquina == 1 and jogada == 2:
    print ('-=-'*10)
    print ('COMPUTADOR JOGOU PEDRA')
    print ('JOGADOR JOGOU PAPEL ')
    print ('-=-'*10)
    print ('JOGADOR VENCEU')
elif maquina == 1 and jogada == 3:
    print ('-=-'*10)
    print ('COMPUTADOR JOGOU PEDRA')
    print ('JOGADOR JOGOU TESOURA')
    print ('-=-'*10)
    print ('MÁQUINA VENCEU')
elif maquina == 2 and jogada ==1:
     print ('-=-'*10)
     print ('COMPUTADOR JOGOU PAPEL')
     print ('JOGADOR JOGOU PEDRA')
     print ('-=-'*10)
     print ('MÁQUINA VENCEU')
elif maquina == 2 and jogada == 3:
    print ('-=-'*10)
    print ('COMPUTADOR JOGOU PAPEL')
    print ('JOGADOR JOGOU TESOURA')
    print ('-=-'*10)
    print ('JOGADOR VENCEU')
elif maquina == 3 and jogada == 1:
    print ('-=-'*10)
    print ('COMPUTADOR JOGOU TESOURA')
    print ('JOGADOR JOGOU PEDRA')
    print ('-=-'*10)
    print ('JOGADOR VENCEU')
elif maquina == 3 and jogada == 2:
    print ('-=-'*10)
    print ('COMPUTADOR JOGOU TESOURA')
    print ('JOGADOR JOGOU PAPEL')
    print ('-=-'*10)
    print ('MAQUINA VENCEU')
else:
    print ('EMPATE')