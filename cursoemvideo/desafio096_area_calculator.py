def area(l, c):
    a = l + c
    print(f'A area de um terreno {l} x {c} é de {a} m2.')


print('Controle de Terrenos')
print('=-'*12)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m):'))
area(l, c)
