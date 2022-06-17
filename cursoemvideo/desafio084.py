temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer Continuar [S/N]? ')).strip().upper()[0]
    if resp in 'N':
        break
print('*'*30)
print(f'Os dados foram {princ}')
print(f'O numero de pessoas cadastradas foi {len(princ)}')
print(f'O maior peso foi {maior} kg. Peso de ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}',)
print()
print(f'O menor peso foi {menor} kg.Peso de ', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')