print ('--='*20)
print ('Analisador de Triângulos')
print ('--='*20)

p1=float(input('Primeiro Segmento: '))
p2=float(input('Segundo Segmento: '))
p3=float(input('Terceiro Segmento: '))

if p1 + p2 > p3 and p2 + p3 > p1 and p3+p1>p2:
    print ("\033[4;34mTais segmentos PODEM FORMAR um triângulo\033[m")
else: 
    print ('\033[34mTais segmentos NÃO PODEM FORMAR um triângulo\033[m')