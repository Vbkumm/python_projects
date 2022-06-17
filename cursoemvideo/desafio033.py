n1 = int(input('diga o primeiro numero: '))
n2 = int(input('diga o segundo numero: '))
n3 = int(input('diga o terceiro numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior numero é {} e o menor numero é {}'.format(maior, menor))
