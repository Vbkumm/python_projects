sala = int(input('Qual valor do seu salario? '))
aum1 = (sala*0.10)+sala
aum2 = (sala*0.15)+sala
if sala>=1250:
    print('seu salario passara para R${}'.format(aum1))
else:
    print('seu salario passara para R${}'.format(aum2))