def leiadinheiro(texto):
    válido = False 
    while not válido:
        entrada = str(input(texto)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


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