def escreva(msg):
    print('{}'.format('~'*(4+len(msg))))
    print(f'  {msg}')
    print('{}'.format('~'*(4+len(msg))))
while True: 
    v = str(input('Escreva uma mensagem: ')).strip()
    escreva(v)
    cond = str(input('Você quer cotinuar? [S/N]')).strip().upper()[0]
    if cond == 'N':
        break