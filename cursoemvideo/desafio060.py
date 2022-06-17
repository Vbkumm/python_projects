print('Calculadora fatorial')
print('='*23)
n = int(input('Diga um numero:'))
print('Calculando fatorial de {} ! = '.format(n),end='')
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x ' if c > 1 else '= ',end='')
    f *= c
    c -= 1
print('{}'.format(f))