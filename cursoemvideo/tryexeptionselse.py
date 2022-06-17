def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('whoops! That is not a number')
            continue
        else:
            print('Thank you!')
            break
        finally:
            print('de qualquer formar apareco')

#ask_for_int()

for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print('numeros e letras sao diferentes')



x = 5
y = 0
try:
    z = x/y
except:
    y=0
finally:
    print('All done')

def transfor_squared():
    while True:
        try:
            t = int(input('Input a integer: '))
        except:
            print('that is not a integer try again!')
        else:
            n = t * t
            print(f'Thank you, your number squared is: {n}')
            break

transfor_squared()