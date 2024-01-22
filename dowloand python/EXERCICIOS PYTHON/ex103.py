def jogador(n='<desconhecido>', g= 0):
       print (f'O jogador {n} fez {g} gol(s)')


#programa principal 
print('-'*20)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Quantos gols ele fez? '))
if gols.isnumeric():
     gols = int(gols)
else: 
     gols = 0
if nome == '':
   jogador(g=gols)
else:
   jogador(nome,gols)
