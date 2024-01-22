from ex111.utilidadesCeV import moeda 
num = float(input('Digite seu salário: R$'))
print(f'Metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Com o aumento de 10%, seu salário passa a ser {moeda.aum(num, 10)}')