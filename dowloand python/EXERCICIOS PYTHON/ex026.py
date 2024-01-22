frase = str (input ('digite uma frase qualquer: ')). upper().strip()

conta= frase.count('A')
posição= frase.find('A')+1
pos_final: frase.rfind('A')+1
print (f'A letra "A" aparece {conta} vezes na frase.')
print (f'A primeira letra "A" apareceu pela primeira vez na posição {posição}')
print (f'A ultima vez que a letra "A" aparece na frase é {pos_final}')


