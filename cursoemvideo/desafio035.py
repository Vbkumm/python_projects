cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'azulclaro':'\033[36m',
         'cinza': '\033[37m'}
print('-='*20)
print('{}analizador de triangulos{}'.format(cores['roxo'],cores['limpa']))
print('-='*20)
r1 = int(input('{}primeira reta'.format(cores['amarelo'])))
r2 = int(input('{}segunda reta'.format(cores['roxo'])))
r3 = int(input('{}terceira reta'.format(cores['cinza'])))
if  r1==r2 and r2==r3:
    print('{} suas retas formam um triangulo Equilatero{}'.format(cores['azul'], cores['limpa']))
elif r1<=r2+r3 and r2==r3 or r2<=r1+r3 and r1==r3 or r3<=r1+r2 and r1==r2:
    print('{} suas retas formam um triangulo Isosceles{}'.format(cores['azul'], cores['limpa']))
elif r1<=r2+r3 and r2<=r1+r3 and r3<=r1+r2 and r1 != r2 and r2 != r3 and r1 != r3:
    print('{} suas retas formam um triangulo Escaleno{}'.format(cores['azul'], cores['limpa']))
else:
    print('suas retas nao formam um triangulo')