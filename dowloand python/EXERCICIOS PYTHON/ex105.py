def notas(*n, sit=False):
    """-> Função para analisar notas e situações de uma turma 
    Para N: quantidade de notas dos alunos(não possui limite)
    Para sit(opicional): Verificar a situação da turma entre ruim, razoável e boa
    return: Dicionário com os dados da turma"""
    dict = {}
    dict['quantidade de notas'] = len(n)
    maior = menor = soma = 0
    for pos, c in enumerate(n):
        if pos == 0: 
            maior = menor = n[pos]
        else: 
            if c > maior:
               maior = c
            if c < menor:
                menor = c
        soma += c
    media = soma/len(n)
    dict ['Média'] = media
    dict['maior'] = maior 
    dict['menor'] = menor
    if sit == True:
       if media < 6:
           dict['situação'] = 'Ruim'
       elif media >= 6 and media <= 7:
           dict['situação'] = 'razoável'
       else: 
           dict['situação'] = 'Boa'
    return dict

#programa principal: 
resp = notas (8.3,7.5,9.7, sit=True)
print(resp)
help(notas)