dados = []
galera =  []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = dados[1]
    else: 
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    cond = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while cond not in 'SN':
        cond = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
print ('-='*30)
print (f'Foram cadastradas {len(galera)} pessoas')
print (f'O maior peso foi {maior}Kg. De: ',end = '')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print (f'O menor peso foi {menor}kg. De: ',end = '')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end = '')