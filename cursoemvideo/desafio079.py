numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Nao adicionado...')
    r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break
print('='*30)
print(f'Voce digitou os valores {sorted(numeros)}')