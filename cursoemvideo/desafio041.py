ano = int(input('Qual ano de nascimento do nadador? '))
if (ano - 2019) < 9:
    print('Mirim')
elif (ano - 2019) < 14:
    print('Infantil')
elif (ano - 2019) < 19:
    print('Junior')
elif (ano - 2019) < 20:
    print('Senior')
elif (ano - 2019) > 20:
    print('Master')