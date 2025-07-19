n = int(input('Digite um número: '))
print(f'TABUADA DO NÚMERO {n}')
print('='*20)
for i in range(1, 11):
    print(f'{n} X {i}: {n * i}')
