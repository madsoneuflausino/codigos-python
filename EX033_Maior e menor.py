n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
#BUSCANDO O MENOR NÚMERO
if n1 < n2 and n1 < n3:
    print(f'\033[7m{n1}\033[m é o menor número.') #com adição de cores
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número.')
if n3 < n2 and n3 < n1:
    print(f'{n3} é o menor número.')

#BUSCANDO O MAIOR NÚMERO
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número.')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número.')
if n3 > n2 and n3 > n1:
    print(f'{n3} é o maior número.')
