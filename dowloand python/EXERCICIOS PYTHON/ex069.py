mais_18 = hom = menos_20 = 0
while True: 
    print ('-'*20)
    print ('CADASTRE UMA PESSOA ')
    print ('-'*20)
    i= int (input('Idade: '))
    sex= str (input('Sexo: [M/F]')).upper().strip()[0]
    while sex not in 'MF':
        sex= str (input('Sexo: [M/F]')).upper().strip()[0]
    print ('-'*20)
    decis = str (input('Quer continuar? [S/N]')).upper().strip()[0]
    while decis not in 'SN':
        decis = str (input('Quer continuar? [S/N]')).upper().strip()[0]
    print ('-'*20)
    if i > 18:
        mais_18 += 1
    if sex == 'M':
        hom += 1
    if sex == 'F' and i < 20:
        menos_20 += 1
    if decis == 'N':
        break
print ('Programa Encerrado')
print (f'''TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {mais_18} 
AO TODO TEMOS {hom} HOMENS CADASTRADOS 
E TEMOS {menos_20} MULHERES COM MENOS DE 20 ANOS''')
