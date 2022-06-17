lista = ('aprender', 'programar', 'linguagem', 'Phyton',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for pos in lista:
    print(f'\nNa palavra {pos.upper()} temos ',end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

