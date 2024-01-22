from lib.interface import *
from lib.arquivo import *#asterisco significa 'tudo'
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True: 
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de ver pessoas cadastradas 
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        Cadastrar(arq, nome, idade)
    elif resposta == 3:
        print(cabeçalho('SAINDO DO SISTEMA...ATÉ LOGO'))
        break
    else:
        print('\033[0;31mERRO. Digite uma opção válida\033[m')
    sleep (2)