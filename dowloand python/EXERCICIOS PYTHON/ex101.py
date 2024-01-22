from datetime import date
#date.today().year
def voto(ano):
    if idade >= 18:
        return ('VOTO ORBIGÁTORIO.')
    elif idade >= 16 and idade < 18 or idade > 60:
        return ('VOTO OPCIONAL.')
    else: 
        return ('VOTO NEGADO.')
#program principal:
print('-'*20)
data = int(input("Qual ano você nasceu: "))
idade = date.today().year - data
r = voto(data)
print(f'Com {idade} anos: {r}')

#Outra forma 
def voto(ano):
    from datetime import date 
    idade = date.today().year - data
    if idade >= 18:
        return f'Com {idade} anos: VOTO ORBIGÁTORIO.'
    elif idade >= 16 and idade < 18 or idade > 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else: 
        return f'Com {idade} anos: VOTO NEGADO.'
#program principal:
print('-'*20)
data = int(input("Qual ano você nasceu: "))
print(voto(data))