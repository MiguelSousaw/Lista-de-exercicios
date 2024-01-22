from random import randint 
from time import sleep
print('Olá, sou seu computador...')
print ('-='*20)
print ('Vou pensar em número entre 0 e 10, tente adivinhar...')
print ('-='*20)

cont = 0
maquina = randint(0,10)
j = int (input('Em qual número eu pensei? '))
while j != maquina:
    print ('PROCESSANDO...')
    sleep (0.5)
    if j < maquina: 
      print ('Mais...Tente mais uma vez')
      j = int (input('Em qual número eu pensei?'))
    if j > maquina: 
       print ('Menos...Tente mais uma vez')
       j = int (input('Em qual número eu pensei? '))
    cont += 1
    

print ('PROCESSANDO...')
sleep (1)
print ('-='*20)
print ('VOCÊ VENCEU!!!')
print (f'Seu número de tentativas até o acerto foram de {cont} vez/vezes')
print ('-='*20)
