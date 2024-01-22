'''def dobra(lista): #lista é somente meu parâmetro base, qnaunto valores é a lista em si, que vai passar a ocupar a função demonstrativa de 'lista'
    pos = 0
    while pos < len(lista):
         lista[pos] *= 2
         pos += 1
valores = [6,3,2,4,1]
dobra(valores)
print(valores)'''

def maior(*num):
    print('-='*30)
    print('Analisando todos os valores passados...')
    for c in num:
        print(c, end = ' ')
    maximo = max(num)
    print(f'Foram informados {len(num)} números ao todo.')
    print(f'O maior valor informado foi {maximo}.')

maior(9,4,3,2,1,5,6)
maior(8,6,3)


#melhor forma de se fazer
def maior(*num):
    print('-='*30)
    print('Analisando todos os valores passados...')
    cont = maximo = 0
    for c in num:
        print(c, end = ' ')
        if cont == 0:
          maximo = c
        else:
          if c > maximo:
            maximo = c
        cont+=1
    print(f'Foram informados {len(num)} números ao todo.')
    print(f'O maior valor informado foi {maximo}.')
maior(9,4,3,2,1,5,6)
maior(8,6,3)
maior ()
