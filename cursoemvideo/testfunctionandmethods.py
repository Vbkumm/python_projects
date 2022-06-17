
import string
def vol(rad):
    volume = (4/3)*(3.14)*(rad**3)
    return volume


print(vol(2))

def ran_check(num, low, high):
    if low < num < high:
        print(f'{num} is in the range between {low} and {high}')


ran_check(5,2,7)


def ran_bool(num, low, high):
    return low < num < high


print(ran_bool(3,1,10))


def up_low(s):
    up = []
    low = []
    x = str(s).strip()
    for z in x:
        if z.isupper():
            up.append(z)
        if z.islower():
            low.append(z)
    print(f'No. of upper case characters: {len(up)}')
    print(f'No. of lower case characters: {len(low)}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(*list):
    lista = []
    for x in list:
        if x not in lista:
            lista.append(x)
    print(lista)

unique_list(1,1,1,1,2,2,3,3,3,3,4,5)


def multiply(*numbers):
    t = 1
    for x in numbers:
        t *= x
    return t


print(multiply(1,2,3,-4))


def palindrome(s):
    x = s.replace(' ','').strip()[::-1]
    return x == s


print(palindrome('helleh'))

def ispang(s, alphabet=string.ascii_lowercase):
    alhpabetset = set(alphabet)
    t = s.strip().lower()
    return alhpabetset <= set(t)

print(ispang('The quick brown fox jumps over the lazy dog'))

