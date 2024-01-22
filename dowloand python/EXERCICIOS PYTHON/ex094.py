pessoas = {}
lista = []
soma1 = 0
while True: 
    pessoas ['nome'] = str(input('Nome: '))
    pessoas ['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoas ['sexo'] not in 'MF':
         pessoas ['sexo'] = str(input('Erro, digite somente M ou F. Sexo: [M/F] ')).strip().upper()[0]
    pessoas ['idade'] = int(input('idade: '))
    soma1 += pessoas['idade']
    lista.append(pessoas.copy())
    conf = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
média = soma1/len(lista)
print (f'B) A média de idade é de {média:.2f} anos')
print ('c) As mulheres cadastradas foram: ', end = '')
for p in lista: #Exemplo claro de quando eu quero algo especifico usando lista e dicionário, é necessário varrer
    if p['sexo'] == 'F':
       print (f'{p["nome"]}', end = '')
print ()
print ('D) Lista de pessoas que estão acima da média:')
'''for p in lista: 
    if p['idade'] > média:
        print(f'  nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')
print ('<='*5, 'ENCERRADO', '=>'*5)'''
for p in lista: #O 'p' corresponde a dicionário, e o lista corresponde a lista que guarda todos os dicionários, nesse programa, abre a possibilidade de haver várias pessoas
    if p ['idade'] > média:
        for k, v in p.items():
          print (f'{k} = {v};', end = '' )