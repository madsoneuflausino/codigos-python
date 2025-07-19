lista = []
for a in range(0, 5):
    n = int(input('Digite um número: '))
    if a == 0 or n > lista[len(lista) - 1]:
        lista.append(n)
        print('Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
        print(f'Número adicionado na posição {pos}')
print(lista)
