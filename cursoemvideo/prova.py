'''Jogo de matematica
soma implementada'''



from random import randint
import time
import datetime


def titulo(msg, cor):
    '''Funcao para colocar cor nos textos e centralizar
    de acordo com o tamanho'''
    tam = 45
    print(f'{cor} '*tam)
    print(f'{cor}    {msg}'.center(tam))
    print(f'{cor} '*tam)


gameres = []
game = {}

while True:
    while True:
        game.clear()
        titulo('VAMOS CALCULAR?', '\33[30;44m')
        print('\33[42;31m')
        game['jogador'] = str(input('  Seu nome: ')).upper().strip()[:12]
        print()
        vitorias = 0
        rad1 = 6
        rad2 = 3
        tempo1 = time.time()
        while True:
            n1 = randint(0, rad1)
            n2 = randint(0, rad2)
            titulo(f'{n1} + {n2} = ', '\33[7;30m')
            print('\33[30m '*30)
            ru = str(input(f'  Resposta =  '))
            print(' '*30)
            rc = n1 + n2
            if ru.isnumeric():
                ru = int(ru)
                if ru == rc:
                    titulo(f'{vitorias+1} acertos', '\33[30;46m')
                    vitorias += 1
                    rad1 += 2
                    rad2 += 3
                else:
                    break
            else:
                break
        tempo2 = time.time()
        tetotal = float(f'{tempo2-tempo1:.0f}')
        game['resultado'] = int(vitorias)
        game['tempo'] = datetime.timedelta(seconds=tetotal)
        titulo('ERRADO', '\33[41;30m')
        print(f'RESPOSTA CERTA ERA {rc}'.center(40))
        print('\33[41m' * 30)
        titulo(f'TOTAL ACERTOS {vitorias} em {game["tempo"]}.', '\33[40;31m')
        if vitorias > 5:
            print('\33[41;30m')
            titulo(f'Parabens {game["jogador"]} você acertou {vitorias} em {game["tempo"]} segundos', '\33[41;30;7m')
            break
        if len(gameres) > 0 and game['resultado'] > gameres[0]['resultado']:
            print('\33[41;30m')
            print(f'NOVO RECORDE {game["resultado"]}  acertos do jogador {game["jogador"]}')
            print('\33[41;30m')
            break
        else:
            if len(gameres) > 0 and game['resultado'] == gameres[0]['resultado'] and game['tempo'] < gameres[0]['tempo']:
                print('\33[41;30m')
                print(f'NOVO RECORDE {game["resultado"]}  acertos do jogador {game["jogador"]}')
                print('\33[41;30m')
                break
            else:
                break
    if game['resultado'] == 0:
        print(f'Nenhum acerto! Tente novamente.'.center(40))
        print()
    else:
        if len(gameres) == 0 or game['resultado'] < gameres[-1]['resultado']:
            gameres.append(game.copy())
        else:
            if game['resultado'] == gameres[-1]['resultado'] and game['tempo'] >= gameres[-1]['tempo']:
                gameres.append(game.copy())
            else:
                p = 0
                while p <= len(gameres):
                    if game['resultado'] > gameres[p]['resultado']:
                        gameres.insert(p, game.copy())
                        break
                    if game['resultado'] == gameres[p]['resultado'] and game['tempo'] <= gameres[p]['tempo']:
                        gameres.insert(p, game.copy())
                        break
                    p += 1
    titulo('RAKING SOMANDO', '\33[30;45m')
    print('Pos', end=' ')
    for i in game.keys():
        print(f'{i:<15}', end='')
    print('\33[30;45m')
    for k, v in enumerate(gameres):
        print(f'{k+1:>3}', end=' ')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()

