'''
num = []
lista = [3, 1, 8]
lista1 = list(range(1,11))
print(lista1)
lista.append(4)
print(lista)
lista.sort()
print(lista)
lista1.pop()
print(lista1)
lista1.pop(3)
print(lista1)
'''
valores = [1 ,5, 9, 13, 18]
for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} achei o valor {v}.')
'''
novalista = []
for cont in range(1,5):
    novalista.append(int(input('Digite um valor: ')))
print(novalista)
'''
# Diferença entre ligação e cópia entre listas
a = [1, 2, 3, 4]
b = a #cria-se assim uma ligação. O que se alterar numa lista altera na outra
c = a[:] # cria-se uma lista b com cópia de todos os valores de a, mas as alteraçõe são individuais
print(a)
print(b)
print(c)
c[2] = 8
print(c)
b [0] = 100
print(a, b)
b.remove(100)
print(a, b)
del(b)
print(a)