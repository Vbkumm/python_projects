nota1 = float(input('qual sua primeira nota: '))
nota2 = float(input('qual sua segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('Reprovado')
elif media < 6.9:
    print('Recuperacao')
elif media > 7.0:
    print('Aprovado')