sexo = str(input('Qual seu sexo [M] [F]?')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos. Por favor informe seu sexo [M] [F]:')).strip().upper()[0]
    if sexo in 'MF':
        print('Seu sexo {} foi registrado com sucesso'.format(sexo))
