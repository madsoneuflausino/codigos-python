tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'\033[34mOs números informados foram:\033[m {tupla}')
print(f'\033[34mO número 9 apareceu\033[m {tupla.count(9)} vez(es).')
if 3 not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número 3 apareceu primeiro na posição {tupla.index(3) + 1}')
print('Os números pares foram:')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')