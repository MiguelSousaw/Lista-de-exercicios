salário= float (input('Qual o salário de um funcionário: R$ '))
aumento = salário * 15/100
valor = salário + aumento
print ('Um funcionário que ganhava {:.2}, com 15% de aumento, passa a receber {:.2}'.format(salário, valor))