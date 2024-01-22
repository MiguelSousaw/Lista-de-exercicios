n1 = float (input ('Me informe qual foi sua primeira nota: '))
n2 = float (input('Me informe qual foi sua segunda nota: '))
n3 = float (input('Me informe qual foi sua terceira nota: '))
n4 = float (input('Me informe qual foi sua quarta nota: '))
media = (n1+n2+n3+n4) / 4
if media < 5:
    print (f'Sua média foi {media:.2}, não atingindo o resultadoesperado, você foi \033[1mREPROVADO\033[m')
elif media > 5 and media < 6.9: 
    print (f'Sua média {media:.2} não foi das melhores, contudo, você ficou de \033[1mRECUPERAÇÃO\033[m')
elif media > 5:
    print (f'\033[32mPARABÉNS, SUA MÉDIA FOI {media:.2} E VOCÊ FOI APROVADO\033[m')