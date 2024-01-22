sal = float ( input ('Qual o salário atual do funcionário? R$ '))
if sal > 1250:
    aum= sal*0.10
    print (f'O salário do funcionário após o aumento passou a ser: {sal+aum}')
else:
    aum2= sal*0.15
    print (f'O salário do funcionário após o aumento passou a ser: {sal+aum2}')