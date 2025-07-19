maior = menor = 0
for i in range(0, 5):
    peso = float(input(f'Peso da {i+1}ª pessoa: '))
    if i == 0:
        maior = menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}Kg')
print('='*40)

# solução usando listas
lista = list()
for i in range(0, 5):
    peso = float(input(f'Peso da {i+1}ª pessoa: '))
    lista.append(peso)
print(f'Maior peso: {max(lista)}Kg')
print(f'Menor peso: {min(lista)}Kg')