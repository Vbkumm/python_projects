lista = [[],[]]
for p in range(1, 8):
    valor = int(input(f'Digite o valor para a {p}º posição: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort
lista[1].sort
print(lista[0])
print(lista[1])
print(lista)


