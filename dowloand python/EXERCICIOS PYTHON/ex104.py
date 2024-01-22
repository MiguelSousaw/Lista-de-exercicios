def leiaint(xt): 
      válido = False 
      while not válido:
          v = input(xt).strip()
          if v.isnumeric():
              v = int(v)
              válido = True
              return v
          else: 
              print(f'\033[0;31mERRO: \"{v}\" é um valor inválido!\033[m')
     
#programa principal:
n = leiaint('Digite um número: ')
print(f'você acabou de digitar o número {n}')
