

def leiaDinheiro(pergunta):
    while True:
        per = input(pergunta)
        x = per.replace(',', '.')
        try:
            float(x)
            x = float(x)
            return x
            break

        except ValueError:
            print(f'\033[31mErro você deve digitar um numero!\033[m')

