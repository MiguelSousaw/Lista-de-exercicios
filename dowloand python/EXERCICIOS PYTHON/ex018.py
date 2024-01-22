import math
n1= float (input('me entrgue um ângulo qualquer: '))
v1= math.sin(math.radians(n1))
v2= math.cos(math.radians(n1))
v3= math.tan(math.radians(n1))
print(f'O seno, cosseno e tangente do ângulo {n1} são respectivamente: {v1:.2}, {v2:.2}, {v3:.2}')

