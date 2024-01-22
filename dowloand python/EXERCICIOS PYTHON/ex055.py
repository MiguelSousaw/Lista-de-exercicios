
'''maior_peso = 0
pessoa_mais_pesada = 0
pessoa_menos_pesada = 0
menor_peso= 200
for i in range (1,6):
    pes = float (input(f'Qual o peso da {i}ª pessoa?'))
    if pes > maior_peso:
      pessoa_mais_pesada = i
      maior_peso = pes
    if pes < menor_peso:
       pessoa_menos_pesada = i
       menor_peso = pes
print (f'A pesssoa mais pesada é {pessoa_mais_pesada}ª pessoa')
print (f'A pessoa mais pesada é a {pessoa_menos_pesada}ª pessoa' )'''

#outra forma 
maior = 0
menor = 0
for i in range (1,6):
   peso = float (input(f'Peso da {i} pessoa: '))
   if i == 1:
      maior = peso
      menor = peso
   else:
    if peso > maior:
         maior = peso
    if peso < menor:
       menor = peso
print (f'O maior peso lido foi de {maior}Kg')
print (f'O menor peso lido foi de {menor}Kg ')