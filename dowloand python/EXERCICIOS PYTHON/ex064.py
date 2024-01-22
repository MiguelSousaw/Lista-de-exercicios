print ('-'*30)
print ('TRATANDO VÁRIOS VALORES')
print ('-'*30)
soma = 0
cont = 0
valor = int(input('DIGITE UM VALOR [DIGITE 999 PARA PARAR]: '))
while valor != 999:
    valor = int(input('DIGITE UM VALOR [DIGITE 999 PARA PARAR]: '))
    cont += 1
    if valor != 999:
      soma += valor #Como funciona a soma? A soma é utilizada como um acumulativo, ao decorrer das repetições, os vários valores irão se adicionando 
print (f'Programa encerrado, foram analisados {cont} termos, cujo a soma é {soma}')