nome = str(input('Digite seu nome completo: ')).strip()
fatia = nome.split() 
nome_final= fatia [len(fatia)-1]
print('seu primeiro nome é: {}'.format (fatia[0]))
print ('Seu  ultimo nome é: {}'.format(nome_final))

           