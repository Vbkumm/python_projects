celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)* temp +32) for temp in celcius]
print(fahrenheit)

fahrenheit = []
for temp in celcius:
    fahrenheit.append((9/5)* temp +32)
print(fahrenheit)

mylist = [x**2 for x in range(0, 11) if x % 2 == 0]
print(mylist)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

mylist = []
for x in [2, 4, 6]:
    for y in [10, 100, 1000]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [1,2,3] for y in [10,100,1000]]
print(mylist)