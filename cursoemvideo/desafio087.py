lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par = col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para a posicao {l}, {c}: '))
print('#'*40)
for l in range(0, 3):
    col += lista[l][2]
    for c in range(0, 3):
        print(f'[{lista[l][c]:^6}]'.center(13), end='')
        if lista[1][c] > maior:
            maior = lista[1][c]
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
print('#'*40)
print(f'A soma dos numeros pares foi {par}')
print(f'A soma dos valores da terceira coluna foi {col}')
print(f'O maior valor da segund linha é {maior}')
