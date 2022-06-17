velo = float(input('qual velocidade: '))
multa = velo - 80
custo = multa * 7
if velo<=80:
    print('velocidade dentro do permitido')
else:
    print('voce foi multado ultrapassou o limite de velocidade em {} km/h'.format(multa))
    print('O valor da multa foi R$ {}'.format(custo))