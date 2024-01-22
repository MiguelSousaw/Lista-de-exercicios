from datetime import date 
totmaior = 0
totmenor= 0
for i in range (1,8):
    ano = int(input(f'Em que ano a {i}ª pessoa  nasceu?'))
    idade = date.today().year - ano 
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print (f'''Ao todo tivemos {totmaior} pessoas que já atinigiram a maior idade
E {totmenor} pessoas ainda são de menor''')
