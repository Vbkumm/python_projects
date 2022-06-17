from random import randint
from time import sleep
from operator import itemgetter
print(f'{"Valores sorteados:":^40}')
print('-='*20)
print()
jogo = {'jog1': randint(1, 6),
        'jog2': randint(1, 6),
        'jog3': randint(1, 6),
        'jog4': randint(1, 6)}
raking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado'.center(40))
    sleep(1)
print()
print('-='*20)
print(f'{"Ranking dos Jogadores":^40}')
print('-='*20)
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(raking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}'.center(40))