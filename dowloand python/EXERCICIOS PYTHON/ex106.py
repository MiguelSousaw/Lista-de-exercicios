c = ('\033m',       #0 - sem cores
     '\033[0;30;41m]', #1 - vermelho 
     '\033[0;30;42m]', #2 - verde
     '\033[0;30;43m]', #3 - amarelo
     '\033[0;30;44m]', #4 - azul
     '\033[0;30;45m]', #5 - roxo
     '\033[7;30m]') #6 - branco)

def titulo(msg, cor=0):
   print(c[cor], end = '')
   print ('~'*(4+len(msg)))
   print (f'  {msg}')
   print ('~'*(4+len(msg)))
   print (c[0], end = '')

def ajuda (com):
    titulo (f'ACESSANDO O MANUAL DE COMANDO \'{com}\'', 4)
    sleep(1)
    print(c[6], end = '')
    help(com)
    print (c[0], end = '')

while True:
   from time import sleep 
   titulo('SITEMA DE AJUDA pyHELP', 2)
   escolha = str(input('Função ou biblioteca > ')).strip()
   ajuda(escolha)
   if escolha.upper() == 'FIM':
      break
titulo('ATÉ LOGO!', 1)