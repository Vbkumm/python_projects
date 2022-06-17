"""
Plus Math Game to everyone who wants to test your math abilities
from beginners to advanced level.

"""

from random import randint
import time
import datetime


def title(msg, cor):
    """ Function to color text and centralize to size.
    input a: message
    input b: color number """
    size = 45
    print(f'{cor} ' * size)
    print(f' {msg}'.center(size))
    print()
    print('\33[m')


def calculator_math():
    """Calculator the math to user.
    Return total hits and last correct answer"""
    hit = 0
    tempo = time.time()
    range_int = 7
    range_end = 0
    while True:
        fist_number = randint(0, range_end)
        second_number = randint(range_end, range_int)
        result = fist_number + second_number
        title(f'{fist_number} + {second_number} = ', '\33[7;32m')
        answer_user = str(input(f'  Resposta =  '))
        print()
        if answer_user.isnumeric():
            answer_user = int(answer_user)
            if result == answer_user:
                title(f'{hit + 1} acertos', '\33[30;46m')
                hit += 1
                range_end += 2
                range_int += 3
            else:
                break
        else:
            break
    title('ERRADO', '\33[41;30m')
    print(f'RESPOSTA CERTA ERA {result}'.center(40))
    print()
    return hit, tempo


def results(hit_tempo):
    """Gives the total timer of the player game and total hits as integer all together as a
    dictionary game"""
    game = {}
    tempo_end = float(f'{time.time() - hit_tempo[1]:.0f}')
    print()
    hits = int(hit_tempo[0])
    tempo_game = datetime.timedelta(seconds=tempo_end)
    if hits == 0:
        title(f'{PLAYER} nenhum acerto! Tente novamente.', '\33[40;31m')
        print()
        return False
    else:
        title(f'O jogador {PLAYER} acertou {hits} em {tempo_game}.', '\33[40;31m')
        game['player'] = PLAYER
        game['hits'] = hits
        game['tempo_game'] = tempo_game
        return game


def game_end(game):
    """Process the gamers list to be organize as most hits in a less time"""
    if not GAMERS or game['hits'] < GAMERS[-1]['hits']:
        GAMERS.append(game.copy())
    else:
        if game['hits'] == GAMERS[-1]['hits'] and game['tempo_game'] >= GAMERS[-1]['tempo_game']:
            GAMERS.append(game.copy())
        else:
            count = 0
            while count <= len(GAMERS):
                if game['hits'] > GAMERS[count]['hits']:
                    GAMERS.insert(count, game.copy())
                    break
                if game['hits'] == GAMERS[count]['hits'] and game['tempo_game'] <= GAMERS[count]['tempo_game']:
                    GAMERS.insert(count, game.copy())
                    break
                count += 1
    return GAMERS


def placar():
    """Gives the results of the game by hits and time"""
    title('RAKING SOMANDO', '\33[30;45m')
    print('\33[30;46m')
    print('Pos', end=' ')
    for i in GAME.keys():
        print(f'{i:<15}', end='')
    print()
    for k, values in enumerate(GAMERS):
        print(f'{k + 1:>3}', end=' ')
        for details in values.values():
            print(f'{str(details):<15}', end='')
        print()
        print()
        print('\33[m')


PLAY_ON = True
GAMERS = []
while PLAY_ON:
    title('VAMOS CALCULAR?', '\33[30;44m')
    PLAYER = str(input('  Qual seu nome? ')).capitalize().strip()[:12]
    print()
    HIT_TEMPO = calculator_math()
    GAME = results(HIT_TEMPO)
    if GAME is False:
        PLAY_ON = True
    else:
        game_end(GAME)
        placar()
    NEW_GAME = input("Quer jogar  de novo [S/N]? ").lower()
    print()
    if NEW_GAME != 's' or NEW_GAME == '':
        PLAY_ON = False
        break
    else:
        PLAY_ON = True
print("Obrigado por jogar!")
