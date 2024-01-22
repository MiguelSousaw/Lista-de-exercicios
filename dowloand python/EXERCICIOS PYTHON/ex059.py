from time import sleep
v1 = int(input('Informe seu primeiro valor: '))
v2 = int(input('Informe seu segundo valor: '))
print ('O menu a seguir indica quais operações possiveis de serem realizadas...')
sleep(1)
print ('''[1] SOMAR 
[2] MULTIPLICAR 
[3] MAIOR 
[4] NOVOS NÚMEROS
[5] SAIR DA OPERAÇÃO''')
sleep(1)
op = int(input('>>>>> Qual sua opção? '))
while op != 5:
    if op == 1:
      soma = v1 + v2
      print (f'O resultado de {v1} + {v2} é igual a {soma} ')
    elif op == 2:
       multi = v1 * v2
       print (f'O resultado de {v1} + {v2} é igual a {multi} ')
    elif op == 3: 
       if v1 > v2: 
          print (f'O maior valor entre {v1} e {v2} é {v1}')
       elif v2>v1:
          print (f'O maior valor entre {v1} e {v2 } é {v2}')
       else: 
          print (f'Os valores {v1} e {v2} são iguais ou incompátiveis')
    elif op == 4:
        v1 = int (input('Qual o primeiro novo número? '))
        v2 = int (input('Qual o segundo novo número? '))
    else:
       print('Número inválido...')
    sleep (1)
    print ('''[1] SOMAR 
[2] MULTIPLICAR 
[3] MAIOR 
[4] NOVOS NÚMEROS
[5] SAIR DA OPERAÇÃO''')
    sleep (1)
    op = int(input('>>>>> Qual sua opção? ')) 
print('<<<<.Programa finalizado.>>>>')