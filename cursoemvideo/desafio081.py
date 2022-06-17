lista = []
pro = ' '
while pro not in 'N':
    lista.append(int(input('Digite um valor: ')))
    pro = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('Nao tem o valor 5 na lista')
