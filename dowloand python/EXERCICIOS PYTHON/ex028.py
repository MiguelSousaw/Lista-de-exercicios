from random import randint #Isso sorteia um número aleátorio
from time import sleep #È uma função na qual faz o computador dormir pelo tempo determinado 
computador= randint(0,5)
print ('--='*20)
print ('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print ('--='*20)
penso = int (input('Em qual número pensei? '))
print ('_PROCESSANDO_')
sleep(2)
if penso == computador:
   print ('PARABÉNS, você conseguiu me vencer!')
else:
   print (f'GANHEI, o número que pensei foi o {computador} e não o {penso}')
   
