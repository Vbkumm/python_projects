

def metade(n=0, formato=False):
    res = n * 0.5
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumentar(n=0, x=0, formato=False):
    res = n + ((n * x)/100)
    return res if not formato else moeda(res)


def diminuir(n=0, x=0, formato=False):
    res = n - (n * x/100)
    return res if not formato else moeda(res)


def moeda(n):
    return f'R$ {n}'

def resumo(n=0, x=0, y=0):
    print('-'*30)
    print(f'Resultado da Moeda'.center(30))
    print('-' * 30)
    print(f'A metade de {moeda(n)} é {metade(n, True)}')
    print(f'O dobro de {moeda(n)} é {dobro(n, True)}')
    print(f'O valor aunentado é {aumentar(n, x, True)}')
    print(f'O valor diminuido é {diminuir(n, y, True)}')