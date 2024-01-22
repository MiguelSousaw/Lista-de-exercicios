time = []
jogador = {}
partidas = []
soma = 0
while True:
    jogador.clear()#Eu apago o jogador anterior para registrar outro jogador
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) 
    partidas.clear()
    for c in range (1, tot+1):
        part = (int(input('{:>27} {}: '.format('Quantos gols na partida', c))))
        partidas.append(part)
        soma += part
    cond = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    jogador['gols'] = partidas[:]
    jogador['total'] = soma
    time.append(jogador.copy())#A cada jogador adcionado, ele vai ser colocado na lista de times
    while cond not in 'SN':
        cond = str(input('Error, digite somente [S/N]. Você quer continuar? ')).strip().upper()[0]
    if cond == 'N':
        break
#resultados
print('-='*30)
print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print ()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-'*40)
#quais dados eu quero mostrar
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 PARA PARAR) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com o código {busca} ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols.')
print('-'*40)
print('=<=< VOLTE SEMPRE >=>=')