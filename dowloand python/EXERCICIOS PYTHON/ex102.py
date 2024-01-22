def fatorial (n, show=False):
    """-> Calcula o fatorial de um número
    para N: O número a ser calculado 
    para Show: função que permite o calculo ser mostrado(True) na tela ou não(False)
    para return: Função que retorna o valor do fatorial de um número n 
          """
    f = 1
    for c in range (n,0,-1):
        f *= c 
        if show==True:
            print(f'{c}', end = '')
            if c > 1:
              print(f' x ', end = '')
            else: 
                print(' = ', end = '')
    return f
#programa principal 
print('-'*20)

print(fatorial(5,show=True ))