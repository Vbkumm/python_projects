
atual = 2019
maior = 0
for pess in range(1,8):
    nasc = int(input('Qual seu ano de nascimento? '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
print('{} atingiram a maior idade e {} nao atingiram'.format(maior, 7-maior))