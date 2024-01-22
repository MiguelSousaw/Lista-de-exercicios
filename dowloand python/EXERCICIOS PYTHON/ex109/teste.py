from ex111.utilidadesCeV import moeda
num = float(input('Digite seu salário: R$'))
print(f'Metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,True)}')
print(f'Com o aumento de 10%, seu salário passa a ser {moeda.aum(num, 10,True)}')
