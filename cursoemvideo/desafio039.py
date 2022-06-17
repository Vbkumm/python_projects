ano = int(input('Diga seu ano de nacimento 4 digitos: '))
if ano == 2001:
    print('Ja esta na hora de voce se alistar')
elif ano > 2001:
    print('Ainda falta {} para voce se alistar'.format(ano-2001))
elif ano < 2001:
    print('Ja passou o prazo do seu alistamento em {} anos'.format(2001-ano))