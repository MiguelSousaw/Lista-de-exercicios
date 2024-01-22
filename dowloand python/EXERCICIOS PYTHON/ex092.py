from datetime import date
pessoa= {}
pessoa ['nome'] = str(input('Nome: ')).strip()
pessoa ['idade'] = date.today().year - int(input('Ano de nascimento: '))  
pessoa ['ctps'] = int (input('Carteira de trabalho (0 não tem): '))
if pessoa ['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano da contratação: '))
    pessoa ['salário'] = float(input('Salário: '))
    pessoa ['aposentadoria'] = pessoa ['idade'] + 15
print ('-='*20)
for k,v in pessoa.items():
    print (f'{k} tem o valor: {v}')