jogador = {}
partidas = []
soma = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) 
for c in range (1, tot+1):
    part = (int(input('{:>27} {}: '.format('Quantos gols na partida', c))))
    partidas.append(part)
    soma += part
jogador['gols'] = partidas[:]
jogador['total de gols'] = soma
print ('-='*30)
print (f'{jogador}')
print ('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print ('-='*30)
print (f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for pos, v in enumerate(partidas):
    print (f'  => Na partida {pos+1} fez {v} gols')
print (f'Foi um total de {soma} gols')