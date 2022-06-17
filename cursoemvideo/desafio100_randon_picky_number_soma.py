from time import sleep
from random import randint
numeros = []
def sorteia(n):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 11)
        print(f'{n}', end=' ', flush=True)
        numeros.append(n)
        sleep(0.4)
    print('PRONTO!')
def pares():
    spa = 0
    for v in numeros:
        if v % 2 == 0:
            spa += v
    print(f'Somando os valores pares de {numeros}, temos a soma {spa}')


sorteia(numeros)
pares()