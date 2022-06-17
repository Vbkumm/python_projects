import random


def gensquares(n):
    for iten in range(n):
        yield iten ** 2

    pass


for x in gensquares(10):
    print(x)


def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)


print('_'*40)
for num in rand_num(1,10,12):
    print(num)


def get_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield  a
        a,b = b,a+b


for number in get_fibon(10):
    print(number)


s = 'hello'

s_iter = iter(s)

for w in s_iter:
    print(w)


my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
