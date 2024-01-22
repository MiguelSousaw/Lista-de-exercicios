print ('='*20)
print ('   10 Termos de uma P.A    ')
print ('='*20)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p1 + (10-1)*r #Essa é a formula de encontra o enesimo termo na matematica 
   
for c in range (p1, decimo, r): #Se colocarmos o número de repetição somente até o dez, minha estrutura entende que eu só quero que se repita até o resultado chegar em dez 
    print (f'{c}', end=' _ ')
print ('ACABOU')
    
