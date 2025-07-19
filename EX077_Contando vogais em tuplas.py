palavras = ('cachorro', 'papagaio', 'camurupim', 'dinossauro',
           'raposa', 'tigre', 'albacora', 'avestruz', 'gato')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'\033[31m{letra}\033[m', end=' ')
