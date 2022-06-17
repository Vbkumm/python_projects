import random
n1 = float(input('Diga um numero de 0 a 5: '))
n2 = random.randint(1,5)
print(n2)
if n1 == n2:
    print('voce acertou')
else:
    print('voce errou')
