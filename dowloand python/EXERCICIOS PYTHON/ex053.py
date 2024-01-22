frase = str (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) 
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto [letra]
print (f'O inverso de {junto} é {inverso}')    
if inverso == junto:
    print (f'A {frase} é um PALINDROMO')
else:
    print (f'A {frase} não é um PALINDROMO')

#outra forma
#inverso = junto [::-1]
  
