def leiaint(xt):
    while True:
        try:
            n = int(input(xt))
        except (ValueError,TypeError):
            print(f'\033[0;31mERRO: Por favor, digite um número inteiro válido. \033[m')
            continue 
        else: 
            return n
def leiafloat(xt): 
    while True:
      try:
        v = float(input(xt))
      except (ValueError,TypeError):
        print(f'\033[0;31mERRO: Por favor, digite um número decimal válido.\033[m')
        continue
      else:
         return v
     
n = leiaint('Digite um número inteiro: ')
print(f'O valor inteiro digitado foi {n}')
n2 = leiafloat('Digite um número decimal: ')
print(f'O valor decimal digitado foi {n2}')
