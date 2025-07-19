lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {max(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor valor é {min(lista)} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')