palavras = 'APRENDER', 'PRORGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO'
for p in palavras:
    print (f'\nNa palavra {p} temos as vogais: ', end = '')
    for letra in p:
        if letra in 'AEIOU': #O comando in se usa apenas com aspas.
            print (letra, end = ' ')



