print('='*30)
print('10 Termos de uma PA')
print('='*30)
p1 = int(input('Primeiro termo: '))
r1 = int(input('Razão: '))
termo = p1
c = 1
total = 0
mais = 10
while mais !=0:
    total=total+mais
    while c <=total:
        print('{} '.format(termo), end='')
        termo += r1
        c += 1
    print('Pausa')
    mais = int(input('quantos termos quer mostrar mais?'))
print('fim')