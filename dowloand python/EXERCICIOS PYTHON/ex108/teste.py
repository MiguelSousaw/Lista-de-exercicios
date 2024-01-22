from ex111.utilidadesCeV import moeda
num = float(input('Digite seu salário: R$'))
print(f'Metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Com o aumento de 10%, seu salário passa a ser {moeda.moeda(moeda.aum(num, 10))}')