print ('-'*30)
print ('SEQUÊNCIA DE FIBONACCI')
print ('-'*30)
termo = int(input('Até quantos termos você quer imprimir? '))
t1 = 0
t2 = 1
cont = 3 #o cont foi utilizado para trazer limite a sequência 
print (f'{t1} -> {t2}', end = '') #usar o print nesse momento foi necessário pq já sabíamos os dois primeiros termos, que sempre serão esses 
while cont <= termo: #somente a partir do terceiro termo que passamos a entrar numa estrutura de repetição 
    t3 = t1 + t2 #na regra de fibnacci o terceiro termo é a soma do antecessor com o antecessor do antecessor. 
    print (f' -> {t3}', end ='')
    t1 = t2 #essa linha e a linha de baixo são necessárias para que haja uma progressão, ou seja, atualização dos resultados 
    t2 = t3
    cont += 1


    
