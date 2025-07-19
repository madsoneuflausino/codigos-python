n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))


print('n1 = {}, n2 = {}'.format(n1, n2))
if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior:')
else:
    print('Os dois números são iguais')