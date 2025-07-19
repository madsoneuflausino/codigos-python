''' MINHA RESOLUÇÃO

lista = []
pares = []
impares = []
for a in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
lista.append(impares)
lista.append(pares)
print(f'Valores ímpares: {lista[0]}')
print(f'Valores pares: {lista[1]}')
'''

lista = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]} e os ímpares são {lista[1]}')
