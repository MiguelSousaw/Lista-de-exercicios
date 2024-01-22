n1 =  int (input('Escreva seu primeiro número: '))
n2 = int (input('Escreva seu segundo número: '))
if n1 > n2:
    print (f'{n1} é maior do que {n2}')
elif n1 < n2:
    print (f'{n2} é maior do que {n1}')
elif n1 == n2:
    print (f'{n1} é igual a {n2}')
else:  
    print ('Error')