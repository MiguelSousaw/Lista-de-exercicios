print ('Gerador de P.A')
print ('-='*15)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
 total += mais
 while cont <= total:
    print (f'{termo} > ', end='')
    termo += r
    cont += 1
 print ('PAUSA')
 mais = int (input('Quantos termos você quer mostrar a mais? '))
print (f'Programa finalizado, no total foram impressos {total} termos ')
