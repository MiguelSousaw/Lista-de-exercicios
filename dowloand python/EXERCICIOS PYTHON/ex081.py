lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cond = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if cond == 'N':
        break
print ('-'*40)
print (f'Foram digitados {len(lista)} elementos!')
lista.sort(reverse=True)
print (f'A lista de valores de forma ordenada descrescente é {lista}')
if 5 in lista:
    print ('O valor 5 foi digitado e está na lista')
else:
    print ('O valor 5 não foi digitado e não está na lista')
    