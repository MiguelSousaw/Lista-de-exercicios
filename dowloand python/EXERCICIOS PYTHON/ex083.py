exps = str(input('Digite a expressão: '))
pilha = []
for simb in exps:
    if simb == '(':
       pilha.append('(')
    elif simb == ')':
       if len(pilha) > 0:
          pilha.pop()
       else:
          pilha.append(')')
          break
if len(pilha) == 0:
   print ('Sua expressão está correta')
else:
   print(f'Sua expressão está errada com {len(pilha)} parenteses em aberto')