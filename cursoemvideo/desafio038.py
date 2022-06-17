num1 = int(input('Escreva um numero inteiro: '))
num2 = int(input('Escreva seu segundo numero inteiro: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1,num2))
elif num1 < num2:
    print('{} é menor que {}'.format(num1,num2))
elif num1 == num2:
    print('Seus numeros sao iguais')