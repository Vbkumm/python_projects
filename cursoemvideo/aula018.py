#galera = [['Joao', 19], ['Maria', 30], ['Pedro', 15], ['Vitor', 17]]
#print(galera[0][0])
#print(galera[1])
#print(galera)
#for p in galera:
#    print(p)
#    print(f'{p[0]} tem {p[1]} anos de idade')
galera = list()
dado = list()
totmai = tatmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        tatmen += 1
print(f'Temos {totmai} maior de idade e {tatmen} menor de idade.')
print('Hellow World'[-3])
