def titulo(msg, cor):
    tam = len(msg) + 4
    print(f'{cor}-'* tam)
    print(f'{cor}  {msg}')
    print(f'{cor}-'* tam)
def proc(texto):
    if texto == 'fim':
        return True
    else:
        titulo(f'Acessando o manual de comando', '\33[47m')
        print('\33[7;30m')
        titulo(f'{help(texto)}', '\33[7;30m')



while True:
    titulo('Sistema de Ajuda PyHELP', '\33[45m')
    s = proc(str(input(f'\33[mFunção ou biblioteca-> ')).strip())
    if s == True:
        break
titulo('Ate logo', '\33[41m')