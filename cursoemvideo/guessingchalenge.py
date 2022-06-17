from random import randint
n = int(randint(0, 100))
jogadas = [0]
print('''Rules: If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!''')
while True:
    r = int(input('Qual o numero?'))
    if 0 > r > 100:
        print("OUT OF BOUNDS")
        r = int(input('Diga um novo numero?'))
    if r == n:
        print(f'You got it ! {len(jogadas)} tried')
        break
    jogadas.append(r)
    if jogadas[-2]:
        if abs(n-r) < abs(n - jogadas[-2]):
            print('mais quente')
        else:
            print('mais frio')
    else:
        if abs(n-r) <= 10:
            print('quente')
        else:
            print('frio')




