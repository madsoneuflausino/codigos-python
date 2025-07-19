from random import *

a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))

lista = [a, b, c, d]
shuffle(lista) # o método "shuffle" embaralha
print(lista)
