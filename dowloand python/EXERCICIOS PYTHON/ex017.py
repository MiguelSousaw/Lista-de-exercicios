import math

n1= float (input('Digite o comprimento do cateto oposto do retângulo: '))
n2= float (input('Digite o comprimento do cateto adjacente do retângulo: '))
hip= math.hypot(n1,n2)
print (f'O valor da hipotenusa é igual a {hip:.2}')