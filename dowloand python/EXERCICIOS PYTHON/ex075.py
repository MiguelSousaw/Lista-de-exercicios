valor = (int(input('Digite o 1ª número: ')),
         int(input('Digite o 2ª número: ')),
         int(input('Digite o 3ª número: ')),
         int(input('Digite o 4ª número: ')),)

print (f'O valor 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
   print (f'O valor 3 aparecu na posição {valor.index(3)+1}ª')
print (f'O(s) número(s) par(es) registrado(s) foi/foram: ', end = '')
for n in valor:#colocando o for dentro da tupla, com essa configuração, o n vai receber os valores colocados
    if n % 2 == 0: 
        print (f'{n}', end = ' ')
        