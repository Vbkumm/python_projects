frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Voce digitou é palindromo')
else:
    print('A frase: {} nao é um palindromo'.format(frase))