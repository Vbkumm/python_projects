numero = ('zero', 'um', 'dois', 'tres', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
user = int(input('Digite um numero entre 0 e 20: '))
while True:
    user = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    if 0<= user <=20:
        break
print(f'Voce digitou o numero {numero[user]}')