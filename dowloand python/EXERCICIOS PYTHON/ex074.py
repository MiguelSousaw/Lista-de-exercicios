from random import randint
valores = randint(0,10), randint(0,10), randint(0,10), randint (0,10), randint(0,10)
print ('Os valores sorteados foram: ', end = '')
for n in valores:
    print (f'{n} ', end = '')
print (f'\nO maior valor sorteado foi {max(valores)}') #A função max te entrega o maior valor encontrado numa tupla #O \n pula para a linha de baixo ignorando completamente o end 
print (f'O menor valor sorteado foi {min(valores)}')