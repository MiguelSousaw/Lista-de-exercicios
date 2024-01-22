num1 = [[0,0,0], [0,0,0], [0,0,0]]#Basicamente nesse exercio todo indice detro de uma lista interna vai receber linha. E toda lista interna dentro da minha lista principal recebera o indice de C. fazendo um esquema de linhas e colunas desta forma
for l in range(0,3):
   for c in range(0,3):
        num1 [l][c] = int(input(f'Digite um valor para [{l} {c}]: ')) 
for l in range (0,3):#Para tres números, uma coluna
    for c in range (0,3):#Um istema de dependencia, a cada tres números escritos conta-se uma linha
        print (f'[{num1[l] [c]:^5}]', end = '')
    print()