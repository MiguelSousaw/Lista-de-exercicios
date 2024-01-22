produtos = 'Lápis',1.75, 'Canetas', 22.30, 'Borracha',2.00, 'Caderno',15.90, 'Estojo',25.00, 'Transferidor',4.20, 'Compasso',9.99,  'Mochila', 120.32, 'Livro', 34.90
print ('-'*40)
print ('{:^40}'.format('LISTAGEM DE PREÇO'))
print ('-'*40)
for pos in range (0,len(produtos)):#usando essa fromade manipular  a tupla. podemos aplicar condições de forma direta
    if pos % 2 == 0: #A condição neste programa me serviu para organizar os valorees, se a posição ocupada fosse par, eu já sabia que seria uma frase escrita, logo, o nome do produto seria alinhado a esquerda, se impar, o número seria alinhado a direita, obrigando escrever todos os valores colocando tudo numa mesma tupla, isso possibilitou o nome e preço ficarem na mesma linha.
        print (f'{produtos[pos]:.<30}', end = '')#Usando o 'produtos' primeiro que a condição significa dizer que vamso ler o produto que está na posição X
    else:
        print(f'R${produtos[pos]:>7.2f}')#centralizado a direita com sete casas #O 2f significa a leitura do número até duas casas decimais após a vírgula 
print ('-'*40)