lista = []
perg = ' '
while perg not in 'N':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('-'*30)
print(f'{"No.":<9}{"Nome":<10}{"Media":>10}')
for i, a in enumerate(lista):
    print(f'{i:<7} {a[0]:<10} {a[2]:>9}')
while True:
    print('-'*30)
    aluno = int(input('Mostrar nota de qual aluno: '))
    if aluno == 999:
        print('FINALIZANDO')
        break
    if aluno <= len(lista) - 1:
        print(f'Notas de {lista[aluno][0]} sao {lista[aluno][1]}')
    print('Volte Sempre')