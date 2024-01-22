valor = []
for c in range (0,5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valor)
menor = min(valor)
print ('-='*30)
print (f'Você digitou os valores: {valor}')
print (f'O maior valor digitado foi {maior} nas posições: ', end= '')
for i,v in enumerate(valor):
    if v == maior:
       print (f'{i}...', end = '')
print ()
print (f'O menor valor foi {menor} nas posições: ', end = '')
for i,v in enumerate(valor):
    if v == menor:
       print (f'{i}...', end = '')