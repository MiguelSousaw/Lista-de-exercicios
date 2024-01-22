a = []
par = []
impar = []
while True:
    v = int(input('Digite um valor: '))
    a.append(v)
    cond = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if v%2 == 0:
        par.append(v)
    else:
        impar.append(v)
    if cond == 'N':
        break
print ('-'*50)
a.sort()
print (f'A lista original é {a}!')
print (f'Os valores pares registrados foram {par}')
print (f'Os valores impares registrados foram {impar}')