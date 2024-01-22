print('Controle de terrenos')
print('-'*20)
def area (L, C):
    a = L * C
    print(f'A área de um terremo {L:.2f}x{C:.2f} é de {a:.2f}m² ')
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)