import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = n1+n2
n4 = int(input('Qual o valor de {} + {}: '.format(n1, n2)))
answer = n3 == n4
if answer == True:
    print('Sua resposta esta correta {}'.format(n3))
else:
    print('Sua resposta esta errada, a correta é {}'.format(n3))