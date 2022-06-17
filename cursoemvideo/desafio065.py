n = soma = cont = maior = menor = 0
media = 1
go = ''
while go in 'Ss':
    n = int(input('Digite um numero: '))
    cont+=1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    go = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma/cont
print('Voce digitou {} numero e a media entre eles foi de {}'.format(cont,media))
print('O menor numero digitado foi {} e o maior foi {}'.format(menor,maior))