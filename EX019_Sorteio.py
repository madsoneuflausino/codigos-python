import random
from math import *
a = str(input('Digite o nome do 1º aluno: '))
b = str(input('Digite o nome do 2º aluno: '))
c = str(input('Digite o nome do 3º aluno: '))
d = str(input('Digite p nome do 4º aluno: '))
sort = random.randrange(1,4)

if sort == 1:
    print(f'O aluno escolhido foi {a}')
elif sort == 2:
    print(f'O aluno escolhido foi {b}')
elif sort == 3:
    print(f'O aluno escolhido foi {c}')
else:
    print(f'O aluno escolhido foi {d}')

# MESMA FUNCIONALIDADE COM LISTA

lista = [a,b,c,d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')