from time import sleep
aluno = []
dados = []
nomef = 'Nome'
mediaf= 'Média'
while True :
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    dados.append(n1)
    dados.append(n2)
    dados.append(media)
    aluno.append(dados[:])
    dados.clear()
    cond = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SsNn':
        cond = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cond == 'N':
        break
print('-='*30)
print('nº'   ,end='     ')
print(f'{nomef:^6}', end = '        ')
print(f'{mediaf:>5}')
print ('-'*30)
for pos, p in enumerate(aluno):
    print (f'{pos}',end = '')
    if aluno[pos][0]:
        print (f'{aluno[pos][0]:^18}',end='')
    if aluno[pos][3]:
        print (f'{aluno[pos][3]:>6.2f}', end = '')
    print ()
print ('-'*40)
while True:
    esc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    for pos, p in enumerate(aluno):
        if esc == pos:
            print (f'Notas de {aluno[pos][0]} são {aluno[pos][1:3]}')
    print ('-'*40)
    if esc == 999:
        break
print ('FINALIZANDO...')
sleep(3)
print('-='*5,'< VOLTE SEMPRE >','-='*5)