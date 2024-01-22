valor = int (input('Digite umn número inteiro: '))
print ('Escolha uma das bases para a conversão: ')
print ('[1] CONVERTER PARA BINÁRIO')
print ('[2] CONVERTER PARA HEXADECIMAL')
print ('[3] CONVERTER PARA OCTAL')
opçao = str(input('Sua opção: '))
if opçao == '1':
   binario = (str(bin(valor)))
   print ('{} convertido para BINÁRIO é igual a {}'.format(valor, binario[2:]))
elif opçao == '2':
   hex = (str(hex(valor)))
   print ('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex[2:]))
elif opçao == '3':
   oct = (str(oct(valor)))
   print ('{} convertido para octal é igual a {}'.format(valor,oct[2:]))
else: 
   print ('Error')