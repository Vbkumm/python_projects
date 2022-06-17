from random import randint
from time import sleep
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^38}')
print('-'*40)
jogo = []
cont = 0
njogo = int(input(f'{"Quantos jogos você quer sortear? ":^36}'))
print()
print('-='*5, f' Sorteando {njogo} jogos', '-='*5)
print()
for sorte in range (0, njogo):
    for n in range(1, 7):
         p = (int(randint(1, 61)))
         if p not in jogo:
             jogo.append(p)
    jogo.sort()
    sleep(1)
    print(f'Jogo {sorte+1}: {jogo}'.center(38))
    jogo.clear()
print()
print('-='*7, 'BOA SORTE', '=-'*7)

