from datetime import date

ano = int (input('Qual o ano? Coloque o 0 caso o ano que você queira analisar seja o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100!=0 or ano % 400==0:
    print (f'O respectivo ano de {ano} é bissexto')
else:
    print (f'O respectivo ano de {ano} não é bissexto')