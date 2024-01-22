from datetime import date

print ('--='*20)
print ('O programa a seguir irá mostrar qando seu alistamento irá acontecer')
print ('--='*20)

data = int (input('Me informe qual o ano do seu nascimento: '))
var = 2023 - data
if var == 18:
    print ('VOCÊ ESTÁ NO MOMENTO CERTO PARA SE ALISTAR')
elif var < 18:
    daquiaanos = 18 - var
    quando = daquiaanos + date.today().year
    print (f'VOCÊ AINDA VAI SE ALISTAR AO SERVIÇO MILITAR DAQUI A {daquiaanos} ANOS! SOMENTE EM {quando}!')
elif var > 18:
    passou = var - 18
    quando2 = date.today().year - passou
    print (f'SEU TEMPO DE SE ALISTAR JÁ PASSOU A {passou} ANOS, O ANO ERA {quando2}!')

else:
    print ('Error')
