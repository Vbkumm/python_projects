def leiaint(msg):
    ok = False
    n = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\33[31mERRO: Digite um numero inteiro valido.\33[m')






n = leiaint('digite um numero:')
print(f'Voce acabou de digitar o numero {n}')