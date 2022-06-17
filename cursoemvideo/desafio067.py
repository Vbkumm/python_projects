n = tabu = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*40)
    for tabu in range(0,10):
        tabu +=1
        print(f'{n} x {tabu} = {n*tabu}')
    print('-'*40)
print('Programa de tabuada encerrado, volte sempre')