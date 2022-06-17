#num = [2, 3, 4, 5]
# num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2g, 2)
#num.pop(2)
#if 4 in num:
#    num.remove(4)
#else:
#    print('nao achei o numero 4')
#num.remove(2)
#print(num)
#print(f'essa lista tem {len(num)} elementos,.')
valores = []
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))
for c, v in enumerate(valores):
    print(f'na posicao {c} econtrei o valor {v}')
print('cheguei ao fim da lista')