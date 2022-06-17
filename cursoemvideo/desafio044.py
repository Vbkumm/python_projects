valor = float(input('Qual valor da compra? '))
print('''Qual opçao de Pagamento?
[1] a vista dinheiro ou cheque
[2] a vista no cartao
[3] 2 x no cartao
[4] 3 x no cartao''')
opcao = int(input('Qual opcao? '))
if opcao == 1:
    print('Valor a ser pago é {}'.format(valor-(valor*.1)))
elif opcao == 2:
    print('Valor a ser pago é {}'.format(valor-(valor * .05)))
elif opcao == 3:
    print('Valor a ser pago é {}'.format(valor))
elif opcao == 4:
    print('Valor a ser pago é {}'.format(valor+(valor * .2)))