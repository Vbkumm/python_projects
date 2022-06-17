nome = str(input('Qual é seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Que nome simples!')
print('Bom dia, {}'.format(nome))

n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>=7.0:
    print('sua media foi boa! parabens')
else:
    print('sua media foi ruim! esdude')