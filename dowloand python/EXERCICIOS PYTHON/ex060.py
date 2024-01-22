'''from math import factorial
print ('O programa a seguir calculará a fatorial do número indicado pelo usuário...')
print ('-='*20)
num = int(input('Digite o número: '))
f = factorial(num)
print(f)'''
from time import sleep 
print ('O programa a seguir calculará a fatorial do número indicado pelo usuário...')
print ('-='*20)
num = int(input('Digite o número: '))
print (f'Calculando fatorial {num}! =', end =" ")
sleep (2)
c = num 
fator = 1 #Tal conceito funciona como a soma, porém, comom o fator nulo da multiplicação é 1, começamos por ele e não por zero
while c > 0:
    print (f'{c}', end=' ')
    print ('x ' if c > 1 else ' = ', end ='')
    fator *= c
    c -= 1
print (f'{fator}')
    
    
    
