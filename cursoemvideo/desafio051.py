print('='*30)
print('10 Termos de uma PA')
print('='*30)
p1 = int(input('Primeiro termo: '))
r1 = int(input('Razão: '))
for c in range(p1, p1+(10*r1), r1):
    print('{}'.format(c), end=' - ')
print('acabou')