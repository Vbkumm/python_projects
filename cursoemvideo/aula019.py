#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 33}
#del pessoas ['sexo']
#pessoas['nome'] = 'vinicius'
#pessoas['peso'] = 90
#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(estado2)
#print(brasil[0]['sigla'])
#print(brasil)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado :'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v} ')
    for v in e.values():
        print(v, end='')
    print()
