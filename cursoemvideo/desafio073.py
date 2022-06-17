time = ('Palmeiras', 'Flamengo', 'Internacional',
        'Grêmio', 'São Paulo', 'Atlético - MG',
        'Athletico - PR', 'Cruzeiro', 'Botafogo',
        'Santos', 'Bahia', 'Fluminense', 'Corinthians',
        'Chapecoense', 'Ceará', 'Vasco', 'Sport',
        'América', 'Vitória', 'Paraná')
print(f'Lista dos times do Brasileirao: {time}')
print('=-'*20)
print(f'Os cinco primeiros times sao {time[0:5]}')
print('=-'*20)
print(f'Os 4 ultimos sao: {time[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabetica {sorted(time)}')
print(f'O Chapecoense esta na {time.index("Chapecoense")+1} posicao')
