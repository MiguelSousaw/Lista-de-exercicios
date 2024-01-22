print ('-=-'*20)
print ('LOJAS WEB FORCE')
print ('-=-'*20)
preço= int (input('Preço em compras: '))
print ('FORMAS DE PAGAMENTO')
print ('[1] à vista dinheiro')
print ('[2] à vista crtão')
print ('[3] 2x no cartão')
print ('[4] 3x ou mais no cartão')
opçao = int (input('Qual é a opção?'))

if opçao == 1:
    valorreal = preço - (preço*0.1 )
    print (f'Sua compra de {preço} vai custar {valorreal:.2} no final')
elif opçao == 2:
    valorreal2= preço - (preço*0.05)
    print (f'Sua compra de {preço}R$ vai custar {valorreal2:.2}R$ no final')
elif opçao == 3:
    print (f'Sua compra vai custar {preço}R$ no final')
elif opçao == 4:
    parcelas = int (input('Quantas parcelas vão ser? '))
    valorreal3= preço + (preço*0.2)
    valorparcela= valorreal3/parcelas
    print (f'Sua compra será parcelada em {parcelas}x de {valorparcela} COM JUROS')
    print (f'Sua compra de R${preço} vai custar R${valorreal3} no final')
else:
    print ('Error')