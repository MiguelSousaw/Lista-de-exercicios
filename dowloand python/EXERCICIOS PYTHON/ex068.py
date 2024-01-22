from random import randint
print ('-='*20)
print ('VAMOS JOGAR PAR OU IMPAR')
print ('-='*20)
cont = 0
while True:
    v_jogador = int(input('Digite um valor:'))
    par_impar= str(input('PAR OU IMPAR? [P/I]')).upper().strip()[0]
    comp = randint(0,11)
    soma = v_jogador+comp
    print ('-'*50)
    print (f'Você jogou {v_jogador} e o computador jogou {comp} e o total deu {soma}.', end = ' ')
    if soma % 2 == 0:
        print (f'{soma} É PAR')
    else: 
        print (f'{soma} É ÍMPAR')
    print ('-'*50)
    if par_impar == 'P' and soma % 2 == 1:
        break
    if par_impar == 'I' and soma % 2 == 0:
        break
    if par_impar == 'P' and soma % 2 == 0:
        print ('VOCÊ VENCEU!')
        cont += 1
    if par_impar == 'I' and soma % 2 == 1:
        print ('VOCÊ VENCEU!')
        cont += 1
    print ('VAMOS JOGAR NOVAMENTE...')
print ('-='*20)
print (f'VOCÊ PERDEU')
print ('-='*20)
print (f'GAME OVER. Você venceu {cont} vez/vezes')