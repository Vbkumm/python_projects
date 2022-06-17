cont = 0
n1 = int(input('Diga um numero inteiro: '))
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[33m',end='')
        cont += 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c), end='')
if cont == 2:
    print('\nEsse numero é primo')
else:
    print('\n\033[32mEsse numero é dividivel por {}'.format(cont))