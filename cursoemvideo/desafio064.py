n=0
n1 = 0
cont=0
while n1!=999:
    n1 = int(input('Digite um numero inteiro ou 999 para finalizar: '))
    if n1!=999:
        cont += 1
        n=n+n1
    else:
        print('Voce digitou {} numeros e a soma entre eles é {}'.format(cont,n))

