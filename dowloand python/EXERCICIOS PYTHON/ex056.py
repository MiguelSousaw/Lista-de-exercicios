h_mais_velho  = 0
soma = 0
maioridadehomem = 0
totmulher20 = 0
for p in range (1,5):
    print (f'-----{p}ª PESSOA-----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    soma += idade
    media = soma/4
    if p == 1 and sexo == 'M':
        h_mais_velho = nome
        maioridadehomem = idade
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        h_mais_velho= nome
        
    if idade < 20 and sexo == 'F':
        totmulher20+=1
print (f'A média de idade do grupo é {media}')
print (f'O homem mais velho tem {maioridadehomem} e se chama {h_mais_velho.upper()}')
print (f'O total de mulheres com menos de 20 anos é de: {totmulher20}')
