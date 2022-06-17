from random import randint
from time import sleep
def analise(* num):
    maior = cont = 0
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(0.5)
        cont +=1
        if maior < v:
            maior = v
    print(f'Foram informados {cont} ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-'*30)


analise(2, 9, 4, 5, 7, 1)
analise(4, 7, 0)
analise(1, 2)
analise(6)
analise()