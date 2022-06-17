valores = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {valores}')
print(f'O valor 9 aparece {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}º posicao')
else:
    print(f'O valor 3 nao aparece em nenhuma posicao')
print('Os valores pares digitados foram: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')