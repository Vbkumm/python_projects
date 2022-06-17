valores = []
maoir = menor = 0
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado na posição ao final da lista')
    else:
        pos = 0
        while pos <= len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição na posicao {valores.index(n)}')
                break
            pos += 1
print(f'Os valores digitados na sua lista sao: {valores}.')
