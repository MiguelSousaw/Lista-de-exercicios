from time import sleep
def contador(a,b,c):
    if c == 0:
        c = 1
    if a > b:
        print('-='*15)
        print(f'Contagem de {a} até {b} de {-c} em {-c}')
        sleep(2.5)
        for d in range(a,b-1,c):
            print(f'{d}', end = ' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        print('-='*15)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        sleep(2.5)
        for d in range(a,b+1,c):
            print(f'{d}', end = ' ', flush=True)
            sleep(0.5)
        print('FIM!')
    contador(1,10,1)
contador(10,0,-2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: ')) 
contador(i,f,p)
