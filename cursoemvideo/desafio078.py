valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {cont} : ')))
#maior = max(valores)
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
#menor = min(valores)
print('=-'*25)
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor digitado foi: {maior} na posicao ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi: {menor} na posicao ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
print()


