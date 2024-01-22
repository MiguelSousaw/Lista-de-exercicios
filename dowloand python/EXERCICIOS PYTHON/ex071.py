print ('='*40)
print ('{:^40}'.format('BANCO SILOÉ'))
print ('='*40)
valor = int(input('Qual valor a ser sacado? R$'))
ced = 50 #limitador 
totcedula = 0 #cont
print ('='*40)
while True:
    if valor >= ced:
        valor -= ced
        totcedula += 1
    else:
        if totcedula > 0:
          print (f'Total de {totcedula} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totcedula = 0
        if valor == 0:
            break
print ('='*40)
print ('VOLTE SEMPRE AO BANCO SILOÉ. TENHA UM BOM DIA!')


