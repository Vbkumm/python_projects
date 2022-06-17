def display_board(*board):
    print('     |   |')
    print(f'   {board[1]} | {board[2]} | {board[3]}')
    print('     |   |')
    print('  -----------')
    print('     |   |')
    print(f'   {board[4]} | {board[5]} | {board[6]}')
    print('     |   |')
    print('  -----------')
    print('     |   |')
    print(f'   {board[7]} | {board[8]} | {board[9]}')
    print('     |   |')



print('-'*20)
print('Jogo da Velha'.center(20))
print('-'*20)
novapartida = ' '
gamers = []
players = {'player': ' ', 'choice': ' ','vitorias': 0}
for x in range(0, 2):
    players['player'] = str(input(f'Nome {x + 1}º jogador: '))
    gamers.append(players.copy())
while gamers[1]['choice'] not in 'XO':
    gamers[1]['choice'] = str(input(f'{gamers[1]["player"]} joga com X ou O? ')).upper().strip()[0]
    if gamers[1]['choice'] == 'X':
        gamers[0]['choice'] = 'O'
    else:
        gamers[0]['choice'] = 'X'
while novapartida not in 'N':
    novapartida = ' '
    j = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(*j)
    gamers.reverse()
    per = 0
    for y in range(1, 10):
        if y % 2 == 0:
            while per not in j:
                per = str(input(f'\33[32m{gamers[0]["player"]}\33[m selecione um numero e marque sua posição: '))
            j.remove(per)
            if per.isnumeric():
                per = int(per)
                j.insert(per, f'\33[32m{gamers[0]["choice"]}\33[m')
                if j[1] == j[2] == j[3] or j[4] == j[5] == j[6] or j[7] == j[8] == j[9] or j[1] == j[4] == j[7] or \
                        j[2] == j[5] == j[8] or j[3] == j[6] == j[9] or j[1] == j[5] == j[9] or \
                        j[3] == j[5] == j[7]:
                    display_board(*j)
                    print(f'Você \33[31m{gamers[0]["player"]}\33[m ganhou')
                    gamers[1]['vitorias'] += 1
                    break
                elif y == 9:
                    print('Empatou!')
                else:
                    display_board(*j)
        else:
            while per not in j:
                per = str(input(f'\33[31m{gamers[1]["player"]}\33[m selecione um numero e marque sua posição: '))
            j.remove(per)
            if per.isnumeric():
                per = int(per)
                j.insert(per, f'\33[31m{gamers[1]["choice"]}\33[m')
                if j[1] == j[2] == j[3] or j[4] == j[5] == j[6] or j[7] == j[8] == j[9] or j[1] == j[4] == j[7] or \
                        j[2] == j[5] == j[8] or j[3] == j[6] == j[9] or j[1] == j[5] == j[9] or \
                        j[3] == j[5] == j[7]:
                    display_board(*j)
                    print(f'Você \33[31m{gamers[1]["player"]}\33[m ganhou')
                    gamers[1]['vitorias'] += 1
                    break
                elif y == 9:
                    print('Empatou!')
                else:
                    display_board(*j)
    print(f'{gamers[0]["player"]} tem {gamers[0]["vitorias"]} vitorias')
    print(f'{gamers[1]["player"]} tem {gamers[1]["vitorias"]} vitorias')
    while novapartida[0] not in 'NS':
        novapartida = str(input('Você quer jogar novamente [S/N]? ')).upper()




