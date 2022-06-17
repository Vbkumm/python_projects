def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 8))


def animal_crackers(texto):
    c = texto.split()
    return c[0][0] == c[1][0]


print(animal_crackers('Za Zae'))


def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


print(makes_twenty(2, 0))


def old_macdonald(name):
    new = ''
    for k, v in enumerate(name):
        if k == 0 or k == 3:
            new += v.capitalize()
        else:
            new += v
    return new


print(old_macdonald('macdonald'))


def master_yoda(text):
    c = []
    for k in text.split():
        c.insert(0, k)
    j = ' '.join(c)
    return j


print(master_yoda('we are ready'))

def master_yoda1(test):
    wordlist = test.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

print(master_yoda1('we are ready'))

def almost_there(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False

print(almost_there(105))


def has_33(*num):
    j = []
    pos = 0
    for n in num:
        j.append(n)
    while pos < len(j):
        if pos > 0 and j[pos] == 3 and j[pos - 1] == 3:
            return True
        else:
            if pos < len(j) -1:
                pos += 1
            else:
                return False


print(has_33(2, 3, 3, 2, 3))


def has_331(*nums):
    for i in range (0, len(nums)-1):
        return nums[i] == 3 and nums[i+1] == 3


print(has_331(2, 3, 3, 2, 3))


def paper_doll(texto):
    novo = []
    for v in texto.strip():
        novo.append(v * 3)
    return ''.join(novo)


print(paper_doll('Mississippi'))


def blackjack(n1, n2, n3):
    bust = 'BUST'
    if (n1+n2+n3) <= 21:
        return (n1+n2+n3)
    else:
        if n1 == 11:
            n1 = 1
            if (n1+n2+n3) <= 21:
                return (n1+n2+n3)
            else:
                return bust
        elif n2 == 11:
            n2 = 1
            if (n1+n2+n3) <= 21:
                return (n1+n2+n3)
            else:
                return bust
        elif n3 == 11:
            n3 = 1
            if (n1+n2+n3) <= 21:
                return (n1+n2+n3)
            else:
                return bust
        else:
            return bust


def blackjack1(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'

print(blackjack(9,9,11))


def summer_69(*n):
    s = []
    pos = 0
    while pos < len(n):
        if n[pos] == 6:
            break
        else:
            s.append(n[pos])
            pos += 1
    while pos < len(n):
        if n[pos - 1] == 9:
            break
        else:
            pos +=1
    while pos < len(n):
        s.append(n[pos])
        pos += 1
    return s

print(summer_69(2, 1, 6, 9, 11, 12 ,13, 14,15))


def summer_691(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


def spy_game(*num):
    py = []
    pos = 0
    while pos < len(num):
        if num[pos] == 7:
            py.append(num[pos])
            pos += 1
            break
        else:
            if num[pos] == 0:
                py.append(num[pos])
                pos += 1
            else:
                pos += 1
    return py == [0,0,7]


print(spy_game(1,0,2,4,0,5,7))


def count_prime(num):
    s = []
    p = []
    pos = 0
    for x in range(1, num + 1):
        s.append(x)
        while pos <= len(s):
            for v in s:
                cont = 0
                for t in range(1, v+1):
                    if v % t == 0:
                        cont += 1
            if cont == 2:
                p.append(v)
                break
            pos +=1
    return len(p)


print(count_prime(100))

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*  * ',
                9:'*    ',10:'* ***', 11:'    ', 12: '    *', 13: '   **', 15: '* *  ', 16: '* * *',
                17: '** **', 18: '**  *', 19: ' **** ', 20:'*  **', 21:' ** *'}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],
                'F':[4,9,5,9,9], 'G':[4,9,10,3,4], 'H': [3,3,4,3,3], 'I': [1,11,1,1,1],
                'J':[13,12,12,3,4], 'K': [3,15,9,15,3], 'L': [9,9,9,9,4], 'M': [3,17,16,3,3],
                'N':[3,18,16,20,3], 'O':[2,3,3,3,2], 'P':[5,3,5,9,9], 'Q':[2,3,3,20,21],
                'R':[5,3,5,15,8]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('R')
