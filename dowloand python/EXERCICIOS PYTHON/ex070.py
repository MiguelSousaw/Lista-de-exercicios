print ('-'*20)
print ('LOJA SUPER BARATÃO')
print ('-'*20)
tot = 0
cont = 0
mais_barato = 0
totmil = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    decis = ' '
    cont  += 1 
    while decis not in 'SN':
        decis = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        print ()
    if cont == 1:
         mais_barato=preço
         barato = produto
    else:
        if preço < mais_barato:
            barato = produto
            mais_barato=preço
    if decis == 'N':
        break
    tot += preço
    if preço > 1000:
        totmil += 1
print ('{:-^40}'.format('FIM DO PRORGRAMA'))
print (f'O total da compra foi: R${tot}')
print (f'Temos {totmil} produto custando mais de R$1000.00')
print (f'O produto mamis barato foi {produto} custando R${preço}')
    
