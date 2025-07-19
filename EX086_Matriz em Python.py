matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'[{l + 1}][{c + 1}] '))
print('=== MATRIZ 3x3 ===')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()