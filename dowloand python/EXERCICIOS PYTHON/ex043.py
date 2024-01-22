print ('-=-'*20)
print ('O programa a seguir vai calcular o seu peso ideal (imc)')
print ('-=-'*20)

peso=float(input('Qual seu peso atual? '))
altura=float(input('Qual a sua altura atual? '))
imc = peso / (altura*altura)
if imc < 18.5:
    print (f'{imc}, Você está ABAIXO do peso')
elif imc >= 18.5 and imc < 25:
    print (f'{imc}, Você está com o peso o IDEAL')
elif imc >= 25 and imc < 30:
    print (f'{imc}, Você está com SOBREPESO')
elif imc == 30 and imc < 40:
    print (f'{imc}, Você está com OBESIDADE')
elif imc > 40:
    print (f'{imc}, Você está com OBESIDADE MÓRBIDA')
