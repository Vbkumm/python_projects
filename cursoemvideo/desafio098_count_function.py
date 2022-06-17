from time import sleep
def conta(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-' * 18)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')


conta(1, 10, 1)
conta(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
conta(ini, fim, pas)
