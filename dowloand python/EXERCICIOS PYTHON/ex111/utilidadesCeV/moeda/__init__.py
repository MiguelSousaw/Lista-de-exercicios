def aum(preço = 0,taxa = 0, sit = False):
    res = (preço * (taxa/100)) + preço 
    return res if sit is False else moeda(res)

def dim (preço=0, taxa = 0,sit=False ):
    res = preço - (preço*(taxa/100)) 
    return res if sit is False else moeda(res)

def dobro(preço= 0, sit = False):
    res = preço * 2
    return res if sit is False else moeda(res)

def metade (preço = 0, sit = False):
    res = preço / 2
    return res if sit is False else moeda(res)
    

def moeda (preço, moeda= 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo (preço=0, aumento=10, redução=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)} ')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aum(preço, aumento,True)}')

