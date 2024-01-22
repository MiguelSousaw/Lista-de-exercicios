print ('--='*20)
print ('Analisador de Triângulos')
print ('--='*20)

p1=float(input('Primeiro Segmento: '))
p2=float(input('Segundo Segmento: '))
p3=float(input('Terceiro Segmento: '))

if p1 + p2 > p3 and p2 + p3 > p1 and p3+p1>p2:
    print ("\033[4;34mTAIS SEGMENTOS PODEM FORMAR UM TRIÂNGULO\033[m")
else: 
    print ('\033[4;34mTAIS SEGMENTOS NÃO PODEM FORMAR UM TRIÂNGULO\033[m')
if p1 == p2 == p3:
    print ('\033[4;34mO TRIÂNGULO É UM EQUILÁTERO, POIS POSSUI TODOS OS LADOS IGUAIS\033[m')
elif p1 == p2 != p3 or p1 == p3 != p2 or p2==p3!=p1:
    print ('\033[4;34mO TRIÂNGULO É ISÓSCELES, POIS POSSUI DOIS LADOS IGUAIS E UM DIFERENTE\033[m')
elif p1!=p2!=p3:
    print('\033[4;34mO TRIÂNGULO É ESCALENO, POIS POSSUI TODOS OS LADOS DIFERENTES\033[m')