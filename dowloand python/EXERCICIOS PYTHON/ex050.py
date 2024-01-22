soma = 0
cont = 0
for c in range (1,7):
    valor = int(input('Digite um valor: '))
    if valor%2==0:
        soma += valor
        cont += 1
print (f'Você informou {cont} NÚMEROS pares e a soma dos números digitados foi {soma}')