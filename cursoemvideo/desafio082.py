lista = []
listapar = []
listaimpar = []
per = ' '
while per not in 'N':
    lista.append(int(input('Digite um numero: ')))
    per = str(input('Quer continuar [S/N]?')).strip().upper()[0]
print(lista)
for p, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista de pares é {listapar}')
print(f'A lista de impar é {listaimpar}')
