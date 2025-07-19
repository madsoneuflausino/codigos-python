import random
tupla = (random.randint(1, 100), random.randint(1,100), random.randint(1, 100),
         random.randint(1, 100), random.randint(1,100))
print('\033[33mEsses foram os números gerados:\033[m')
for n in tupla:
    print(n, end=' ')
print(f'\nO maior valor foi: {max(tupla)}')
print(f'O menor valor foi: {min(tupla)}')