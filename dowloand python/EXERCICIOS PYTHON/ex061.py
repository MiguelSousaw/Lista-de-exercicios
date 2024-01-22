print ('Gerador de P.A')
print ('-='*15)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
termo = p1
cont = 1
while cont <= 10:
    print (f'{termo} > ', end='')
    termo += r
    cont += 1
print ('fim')
    
