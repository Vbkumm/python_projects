cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}
casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu salario? '))
parcelas = int(input('Em quanto anos voce vai pagar? '))
numpar = parcelas*12
prestacao = casa / numpar
if prestacao >= 0.3*salario:
    print('O valor da prestação é {} e compromete mais que 30% do seu salario que é de {}'.format(prestacao,salario))
    print('{}Seu emprestimo foi negado{}'.format(cores['vermelho'],cores['limpa']))
else: print('{}Seu emprestimo foi aprovado{}'.format(cores['verde'],cores['limpa']))
