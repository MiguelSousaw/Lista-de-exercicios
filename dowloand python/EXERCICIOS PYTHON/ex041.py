from datetime import date
print ('A Confederação Nacional de Natação precisa do seu ano de nascimento para rotular em qual categoria você se encaixa')
ano= int (input('Em qual ano você nasecu? '))
result = date.today().year - ano
if result <= 9:
    print ('Sua categoria é a mirim')
elif result <= 14:
    print ('Sua categoria é a infantil')
elif result <= 19:
    print ('Sua categoria é a júnior')
elif result <= 25:
    print ('Sua categoria é a sênior')
elif result > 25:
    print  ('Sua categoria é a master')
else:
    print ('Error')