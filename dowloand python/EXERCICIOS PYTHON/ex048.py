soma = 0 #tal recurso é chamado de acumuylador, age diferente de uma variável/ Acumula os valores
cont = 0 #um contador soma o valor referente a um / Conta quantos valores referentes foram achados  
for n in range (1,501, 2):
    if n%3==0:
      soma += n #Usar o mais e o menos antes do igual significa que ele ou vai somar ou vai subtrair dele mesmo 
      cont += 1
print (f'A soma de todos os {cont} valores é {soma}')

      