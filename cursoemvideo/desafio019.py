import random
n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')
n5=[n1, n2, n3, n4]
print('O escolhido foi {}'.format(random.choice(n5)))
print(random.sample(n5, len(n5)))