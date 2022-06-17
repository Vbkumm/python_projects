from random import randint
print('=-'*15)
print('Vamos jogar par ou impar')
print('-='*15)
cont1 = 0
while True:
    jog1 = int(input('Diga um numero de 0 a 10: '))
    jog2 = randint(1,10)
    total = jog1 + jog2
    esco = ' '
    while esco not in 'PI':
        esco = str(input('Par ou Impar [P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jog1} e o computador {jog2}. Total {total}. ')
    print('\33[31;42mDeu Par\33[m'if total % 2 == 0 else '\33[32;41mDeu Impar\33[m')
    if esco == 'P':
        if total % 2 == 0:
            print('\33[35;41mVoce Venceu!\33[m')
            cont1 += 1
        else:
            print('Voce Perdeu')
            break
    elif esco == 'I':
        if total % 2 == 1:
            print('\33[35;41mVoce Venceu!\33[m')
            cont1 += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos Jogar novamente...')
print('=-'*15)
print(f'GAME OVER! Voce venceu {cont1} vezes')


