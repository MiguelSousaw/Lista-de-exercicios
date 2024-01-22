n = 0
cont = 0
soma = 0
while True:
   n = int(input('Digite um número: '))
   if n == 999: #O break precisa ver antes dda soma e contagem se você quiser desconsidera-lo 
      break
   soma += n
   cont += 1
   
print (f'A soma vale {soma} e a quantidade de termos é {cont}')
