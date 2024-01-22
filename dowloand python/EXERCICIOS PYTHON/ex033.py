n1 = int (input('Primeiro Número: '))
n2 = int (input('Segundo Número: '))
n3 = int (input('Terceiro Número: '))

if n1 < n2 and n1 < n3 and n3 > n2:
    print (f'O menor valor é: {n1}')
    print (f'O maior valor é: {n3}')
elif n1 < n2 and n1 < n3 and n2 > n3:
    print (f'O menor valor é: {n1}')
    print (f'O maior valor é: {n2}')
elif n2 < n1 and n2 < n3 and n3>n1:
    print (f'O menor valor é {n2}')
    print (f'O maior valor é {n3}')
elif n2 < n1 and n2 < n3 and n1>n3: 
    print (f'O menor valor é {n2}')
    print (f'O maior valor é {n1}')
elif n3 < n1 and n3 < n2 and n1 > n2:
    print (f'o menor valor é: {n3}')
    print (f'O maior valor é: {n1} ')
elif n3 < n1 and n3 < n2 and n2 > n1:
    print (f'o menor valor é: {n3}')
    print (f'O maior valor é: {n2} ')