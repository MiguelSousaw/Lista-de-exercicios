from time import sleep
while True:
    print ('-='*20)
    print ('Digite um valor para ver sua tabuada')
    print ('-='*20)
    num = int(input('Valor: '))
    if num < 0:
        break
    print ('-'*20)
    print (F'TABUADA DE {num}:')
    for c in range (1,11):
        result = num*c
        print (f'{num} x {c} = {num}')
    print ('-'*20)
    sleep (3)
print ('PROGRAMA ENCERRADO. VOLTE SEMPRE!')