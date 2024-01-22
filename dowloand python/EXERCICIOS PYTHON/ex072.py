#O exercicio a sgeuir atribui o valor digitado pelo usuário ao seu valor por extenso, e com isso não precisamos de for, somente puxando ultilizando colchetes conseguimos fazer esssa atribuição.

número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
valor = ''
while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    if 0 <= valor <= 20 :
        break
    print ('Tente novamente.', end = '')
print (f'Você digitou o número {número[valor]}')



