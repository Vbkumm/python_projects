from datetime import datetime
trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
while True:
    trabalhador['carteira'] = int(input('Carteira de Trabalho (0 nao tem): '))
    if trabalhador['carteira'] != 0:
        trabalhador['ctps'] = int(input('Ano de contratação: '))
        trabalhador['salario'] = float(input('Salario: R$ '))
        trabalhador['aposetadoria'] = (trabalhador['ctps'] + 35) - datetime.now().year + trabalhador['idade']
        break
    else:
        break
print(trabalhador)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
