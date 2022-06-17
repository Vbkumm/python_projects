def jogador(j='', n=0):
    j = str(input('Nome do Jogador:'))
    n = str(input('Numero de Gols: '))
    if n.isnumeric():
        n = int(n)
    else:
        n = 0
    if j.strip() == '':
        j = 'desconhecido'
    print(f'O jogador {j} fez {n} gol(s) no campeonato')


jogador()