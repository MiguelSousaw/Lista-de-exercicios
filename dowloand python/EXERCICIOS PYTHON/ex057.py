sexo = str (input('Qual seu sexo? [M/F] ')).upper()
while sexo != 'M' or sexo != 'F':
    sexo = str (input('Dados inválidos. Por favor,qual seu sexo? [M/F]')).upper()
print ('RESULTADO ANALISADO!')