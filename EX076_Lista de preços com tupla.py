produtos = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Tranferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.20, 'Caneta', 11.00,
            'Livro', 112.45)
print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)
for cont in range(len(produtos)):
    if cont % 2 == 0:
        print(f'\033[36m{produtos[cont]:.<25}\033[m', end='')
    else:
        print(f'R${produtos[cont]:>8.2f}')