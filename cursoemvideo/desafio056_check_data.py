somaidade = 0
maioridade = 0
nomevelho = ''
mulhermenor = 0
for p in  range(1,5):
    print('-'*5,'{}º Pessoa'.format(p),'-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulhermenor += 1
print('A media das idades é {}'.format(somaidade/4))
print('O homem mais velho é {} e sua idade é {}'.format(nomevelho, maioridade))
print('O Grupo possui {} mulheres menores de 20 anos'.format(mulhermenor))