print ('-'*30)
print ('TRATANDO VALORES')
print ('-'*30)
valor = 0
sugest = 'S'
media = 0
cont = 0
soma = valor 
media = 0
maior_valor = 0
menor_valor = 0
while sugest == "S":
     valor = int (input('DIGITE UM VALOR: '))
     sugest = str (input('Você quer prosseguir [S/N]? ')).upper().strip()[0]
     cont += 1
     soma += valor
     media = soma/cont
     if cont == 1:
          maior_valor = menor_valor = valor 
     else:
          if valor > maior_valor:
               maior_valor=valor
          if valor < menor_valor:
               menor_valor=valor
print (f'PROGRAMA ENCERRADO. {cont} Termos foram digitados, cujo a soma entre eles é de {soma}.')
print (f'A média registrada entre todos os termos é de {media} e o maior valor é {maior_valor} e o menor é {menor_valor}')



