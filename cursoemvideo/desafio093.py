futebol = {}
partidas = []
tgol = 0
futebol['nome'] = str(input('Nome do jogador: '))
futebol['gols'] = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
if futebol['gols'] > 0:
    for c in range(1, futebol['gols'] +1):
        futebol['total'] = int(input(f'Quantos gols na partida {c}º? '))
        partidas.append(futebol['total'])
        tgol += futebol['total']
print('=-'*30)
futebol['gols'] = partidas
futebol['total'] = sum(partidas)
print(futebol)
print('=-'*30)
for k, v in (futebol.items()):
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {futebol["nome"]} jogou {len(partidas)} partidas.')
for c in enumerate(partidas):
    print(f'Na partida {c[0]+1}, fez {c[1]} gols.')
print(f'Foi um total de {tgol}')
print('-='*30)



