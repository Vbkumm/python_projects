pessoa = {}
grupo = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'FM':
        pessoa['sexo'] = str(input('ERRO! Por favor, digite apenas M ou F: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    nova = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    while nova not in 'SN':
        nova = str(input('ERRO! Responda apenas S ou N: ')).strip().upper()[0]
    if nova in 'N':
        break
media = soma / len(grupo)
print('=-'*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A media de idade do grupo e {media:5.2f}.')
print('- As mulheres cadastradas no grupo sao: ', end='')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('- Lista das pessoas que estao acima da media:')
for i in grupo:
    if i['idade'] > media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('<<ENCERRADO>>')
