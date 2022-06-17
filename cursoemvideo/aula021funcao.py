def fatoria(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatoria(5)
f2 = fatoria(4)
f3 = fatoria()

f4 = input(input(f'digite um numero'))
print()

