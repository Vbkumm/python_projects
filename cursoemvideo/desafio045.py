import random
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
joga = int(input('Qual sua jogada? '))
jogaco = random.randint(0,2)
print('Computador joga {}'.format(jogaco))
if joga == 0 and jogaco == 1 or joga == 1 and jogaco == 2 or joga == 2 and jogaco == 0:
    print('Computador Venceu')
elif joga == 1 and jogaco == 0 or joga == 2 and jogaco == 1 or joga == 0 and jogaco == 2:
    print('Voce venceu')
else:
    print('Empatou')