print('Calculadora de dois numeros')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = 0
while n3!= 5:
    print('''Qual operação fazer?
    [1] somar
    [2] multiplicar
    [3] qual maior?
    [4] novos numeros
    [5] sair da calculadora''')
    n3 = int(input('Digite a operação: '))
    if n3 == 1:
        print('O resultado da soma entre {} e {} é {}.'.format(n1,n2,n1+n2))
    elif n3 == 2:
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1,n2,n1*n2))
    elif n3 == 3:
        if n1 > n2:
            print('O maior numero é {}'.format(n1))
        else:
            print('O maior numero é {}'.format(n2))
    elif n3 == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif n3 == 5:
        print('Fim')