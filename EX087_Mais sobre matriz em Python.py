matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'[{linha + 1}][{coluna + 1}] '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end=' ')
    print()
soma = terceira = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
print(f'A soma dos valores pares é {soma}')
for linha in range(0, 3):
    terceira += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {terceira}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
print(f'O maior valor digitado na 2ª linha foi {maior} ')