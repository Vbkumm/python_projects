prec = total = pro1000 = conta = barato = 0
prodba = ' '
print('-'*20)
print('Loja compras')
print('-'*20)
while True:
    prod = str(input('Nome do produto: ')).strip().upper()
    prec = float(input('Valor do produto: '))
    total += prec
    conta += 1
    cont = ' '
    if prec > 1000:
        pro1000 +=1
    if conta == 1 or prec < barato:
        barato = prec
        prodba = prod
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*10,'Fim das compras','-'*10)
print(f'''O total da compra foi R$ {total}.
Temos {pro1000} custando mais de R$ 1000,00.
O produto mais barato foi {prodba}''')