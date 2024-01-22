nome = str(input ('Digite seu nome; ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letra = len(nome)-nome.count(' ')
divisor= nome.split()
result= divisor [0]
letras2= len (result)


print (f"""Analisando seu nome...
    Seu nome em maiusculo é {maiusculo}
    Seu noome em minusculo é {minusculo}  
    Seu nome tem ao todo: {letra} letras
    Seu primeiro nome é {result} e ele tem {letras2} letras""" )