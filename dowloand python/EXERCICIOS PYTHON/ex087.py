#A SOMA DOS VALORES PARES DIGITADOS
# A SOMA DOS VALORES DA TERCEIRA COLUNA
#O MAIOR VALOR DA SEGUNDA LINHA
num1 = [[0,0,0], [0,0,0], [0,0,0]]#Basicamente nesse exercio todo indice detro de uma lista interna vai receber linha. E toda lista interna dentro da minha lista principal recebera o indice de C. fazendo um esquema de linhas e colunas desta forma
par = soma = maior = 0
pares = []
for l in range(0,3):
   for c in range(0,3):
        num1 [l][c] = int(input(f'Digite um valor para [{l} {c}]: ')) 
        if num1 [l][c] %2 == 0:
            pares.append(num1[l][c])#lista de valores pares
        
        #O p rogram abaixo serve para descobrimos se o valor digitado foi par, ainda é possivelsabermos quais foram os numeros pares digitados usando a função append
        if num1[l][c] % 2 == 0:
            par += num1[l][c]

print ('-='*30)
for l in range (0,3):#Para tres números, uma coluna
    for c in range (0,3):#Um istema de dependencia, a cada tres números escritos conta-se uma linha
        print (f'[{num1[l] [c]:^5}]', end = '')
    print()
print ('-='*30)
print (f'A soma de valores pares digitados é: {par}')
for l in range (0,3):
    soma += num1[l][2]
print (f'A soma dos valores da terceira coluna é: {soma}')
for c in range (0,3):
    if c == 0 or num1[1][c] > maior:
        maior = num1[1][c]
print (f'O maior valor da segunda linha é {maior}.')
print (f'Os valores pares digitados nessa matriz foram: {pares}')
#Para analisarmos uma coluna ou linha em detrimento de outra, precisamos analisar qual delas será a fixa e varrer usando uma estrutura de repetição!