cont18 = contho = contm20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        cont18 +=1
    sexo = ' '
    segu = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            contho += 1
        elif sexo == 'F' and idade < 20:
            contm20 += 1
    print('-' * 20)
    while segu not in 'SN':
        segu = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if segu == 'N':
        break
print(f'''Cadastro encerrado com um total de {cont18} pessoas com mais de 18 anos.
 Ao todo tem {contho} homens cadastrados.
 E temos {contm20} mulheres com menos de 20 anos.''')
