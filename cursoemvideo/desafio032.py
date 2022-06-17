dist = float(input('qual distancia da sua viagem? '))
pr1 = dist * 0.5
pr2 = dist * 0.45
if dist<=200:
    print('Sua viagem foi curta o preço é R${}'.format(pr1))
else:
    print('Sua viagem foi longa o preço é R${}'.format(pr2))