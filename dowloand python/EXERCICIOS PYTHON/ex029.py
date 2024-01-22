v = int(input ('Qual a velocidade de um carro? '))
if v <= 80:
  print ('Tenha um Bom dia! Dirija com segurança!')
else: 
  print('Você foi multado por ultrapassar os limites da lei de trânsito.')
  multa= (v - 80)*7
  print ('O valor de sua multa foi: {}. Dirija com mais responsabilidade da próxima vez!'.format(multa))