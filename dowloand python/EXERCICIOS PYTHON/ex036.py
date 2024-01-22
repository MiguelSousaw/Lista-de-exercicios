valorcasa = int (input ('Qual o valor da casa? R$ '))
salario = int (input ('Qual o salário do comprador? R$ '))
anos = int (input ('Em quantos anos o comprador irá pagar a casa? '))
preço = valorcasa / (anos*12)
if preço > salario*0.3:
    print ('Para pagar uma casa de {} em {} anos a prestação será de {:.2} '.format (valorcasa, anos, preço))
    print ('Empréstimo \033[1mNEGADO\033[m')
else:
    print ('Para pagar uma casa de {} em {} anos a prestação será de {:.2} '.format (valorcasa, anos, preço))
    print ('Empréstimo \033[1mCONCEDIDO\033[m')