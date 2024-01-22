viagem = int (input('Qual a distância da viagem: KM '))
if viagem <= 200:
    valor = viagem*0.5
    print (f'O valor da sua viagem é de: {valor}R$')
else: 
    valor2= viagem*0.45
    print (f'O valor da sua viagem é de: {valor2}R$')