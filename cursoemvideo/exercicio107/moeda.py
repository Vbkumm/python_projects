def metade(n=0, formato=False):
    res = n - (n * n/100)
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

def resumo(p, x, y):
    print(f'A metade de {moeda(p)} é {metade(p, True)}')
    print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
    print(f'O valor aunentado é {aumentar(p, x, True)}')
    print(f'O valor diminuido é {diminuir(p, y, True)}')