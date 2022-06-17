#def soma(a, b):
  #  print(f'A = {a} e B = {b}')
 #   s = a + b
 #   print(f'A soma A + B = {s}')


#soma(b=4, a=5)
#soma(7, 5)
#def contador(* núm):
#    tam = len(núm)
#    print(f'Recebi os valores {núm} e sao ao todo {tam} numeros')


#contador(2, 3, 7)
#contador(6, 4)
#contador(3, 4, 5, 6, 7)
#def dobra(lista):
#    pos = 0
#    while pos < len(lista):
#        lista[pos] *=2
 #       pos += 1


#valores = [2, 3, 4, 5, 6, 7]
#dobra(valores)
#print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 3, 4, 5)

