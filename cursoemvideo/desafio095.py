jogador = {}
time = []
ngol = []
prox = ' '
while prox not in 'N':
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partdidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    ngol.clear()
    if jogador['partdidas'] > 0:
        for c in range(1, jogador['partdidas']+1):
            ngol.append(int(input(f'Quantos gols na partida {c}? ')))
            jogador['gols'] = ngol[:]
            jogador['total'] = sum(ngol)
        time.append(jogador.copy())
    prox = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('=-' * 27)
    if prox not in 'SN':
        prox = str(input('ERRO! Responda S ou N? '))
print('-'*55)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*55)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*55)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para finalizar]'))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Nao exite jogador com esse condigo {busca}')
    else:
        print(f'---Levantamento do jogador {time[busca]["nome"]}:---')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*50)
print('Volte sempre')

