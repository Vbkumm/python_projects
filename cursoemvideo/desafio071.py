print('CAIXA ELETRONICO'.center(30))
print('='*30)
saque = int(input('Qual valor a ser sacado? R$ '))
total = saque
ced = 50
toced = 0
while True:
    if total >= ced:
        total -= ced
        toced += 1
    else:
        if toced > 0:
            print(f'Total de {toced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        toced = 0
        if total == 0:
            break