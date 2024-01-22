num = [[ ], []]
for c in range (1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor %2 == 0:
        num[0].append(valor)
    elif valor %2 == 1:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print ('-='*30)
print (f'Todos os valores: {num}')
print (f'Os valores pares digitados e adcionados na lista são: {num[0]}')
print (f'Os valores impares digitados e adicionados na lista foram: {num[1]}')