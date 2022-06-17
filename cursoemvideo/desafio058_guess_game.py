import random
n1 = int(input('Digite um numero de 0 a 10: '))
n2 = random.randint(0,10)
conta = 1
while n1!=n2 or n1>10:
    n1 = int(input('Voce errou computador jogou {}, tente novamente. Digite um numero de 0 a 10: '.format(n2)))
    n2 = random.randint(0,10)
    conta += 1
if n1 == n2:
    print('Computador jogou {} voce acertou em {} tentativas'.format(n2,conta))
