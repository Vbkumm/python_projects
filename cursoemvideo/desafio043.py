peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura*altura)
pesoideal = (24.9*(altura*altura))
pesoidealm = (18.6*(altura*altura))
if imc<18.5:
    print('Seu imc é {} voce esta abaixo do peso! Seu peso ideal é {}'.format(imc,pesoidealm))
elif imc<25:
    print('Seu imc é {} voce esta no peso ideal!'.format(imc))
elif imc<30:
    print('Seu imc é {} voce esta com sobrepeso! Seu peso ideal é {}'.format(imc,pesoideal))
elif imc<40:
    print('Seu imc é {} voce esta obeso!'.format(imc))
else:
    print('Seu imc é {} voce esta na obesidade morbida! Seu peso ideal é {}'.format(imc,pesoideal))