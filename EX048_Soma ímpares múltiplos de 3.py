s = 0
for i in range(3, 500, 2): #pegando todos os valores ímpares de 3 até 500
    if i % 3 == 0: #verificando se o número é múltiplo de 3
        s += i
print(f'A soma de todos os múltiplos de 3, indo de 3 a 500 é {s}')
