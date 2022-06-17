from datetime import datetime


def voto(ano):
    voto = ''
    idade = datetime.now().year - ano
    if idade < 16:
        voto = 'NAO VOTA'
    elif idade >= 16 and idade < 18 or idade >= 65:
        voto = 'OPCIONAL'
    elif idade >= 18:
        voto = 'OBRIGATORIO'
    print(f'Com {idade} anos: {voto}')


ano = int(input('Em que ano voce nasceu 4 digitos? '))
voto(ano)