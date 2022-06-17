n = soma = cont = resu = 0
while True:
    n = int(input('Diga um numero a ser somado: '))
    print('=-' * 20)
    soma +=n
    resu = int(input('Qual resultado? '))
    if soma == resu:
        cont += 1
        print(f'\33[7;34mTotal soma é {soma} \33[m',end='')
    else:
        print(f'Voce errou a soma, mas acertou {cont} vezes anteriormente')
        print('=-'*20)
        break