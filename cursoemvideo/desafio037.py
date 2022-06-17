numero = int(input('Diga um numero inteiro: '))
conver = int(input('Para transformar em binario digite 1, para octal digite 2 e para hexadecimal 3: '))
bina = bin(numero)
octa = oct(numero)
hexa = hex(numero)
if conver == 1:
    print('Seu binario é {} '.format(bina))
elif conver == 2:
    print('Seu octal é: {}'.format(octa))
elif conver == 3:
    print('Seu hxadecimal é: {}'.format(hexa))
else:
    print('Voce selecionou a opcao errada!')