colegio = {}
colegio['nome'] = str(input('Nome: '))
colegio['media'] = float(input(f'Media de {colegio["nome"]}: '))
print(f'Nome é igual a {colegio["nome"]}.')
print(f'Media é igual a {colegio["media"]}')
if colegio['media'] >= 7:
    colegio['situacao'] = 'Aprovado'
elif colegio['media'] >= 5 and colegio['media'] < 7:
    colegio['situacao'] = 'Recuperaçao'
else:
    colegio['situacao'] = 'Reprovado'
print(f'Situaçao é igual a {colegio["situacao"]}')