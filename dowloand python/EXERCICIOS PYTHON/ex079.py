num = []
while True:
    v = int(input('Digigte um valor: '))
    cond = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if v not in num:
        num.append(v)
        print ('Valor adcionado com sucesso!')
    else:
        print ('Valor duplicado, não vou adcionar...')
    if cond == 'N':
        break
print ('-='*30)
num.sort()
print (f'Você digitou os valores: {num}')