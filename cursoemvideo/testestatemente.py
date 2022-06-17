st = 'Print only the words that start with s in this sentence'
palavras = [st.split()]
s = []
for x in palavras:
    for y in x:
        if str(y).strip()[0] == 's':
            print(y)

for x in range(0,11,2):
    print(x, end=' ')
print()


lista = [x for x in range(0,51) if x % 3 == 0]
print(lista)

st = 'Print every word in this sentence that has an even number of letters'
pala = [st.split()]
for x in pala:
    for y in x:
        if len(y) % 2 == 0:
            print('even', end=' ')
        else:
            print(y, end=' ')
print()

n = []
for j in range(0, 101):
    if j % 3 == 0 and j % 5 == 0:
        print('FizzBuzz', end=' ')
    elif j % 3 == 0:
        print('Fizz', end=' ')
    elif j % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(j, end=' ')
print()


st = 'Create a list of the first letters of every word in this string'
n = [x[0] for x in st.split()]
print(n)

def myfunc(string):
    result = ''
    for j in string.split():
            for k, v in enumerate(j):
                if k % 2 == 0:
                    result += v.upper()
                else:
                    result += v.lower()
            return result

print(myfunc('fasdfasdfasfa'))
