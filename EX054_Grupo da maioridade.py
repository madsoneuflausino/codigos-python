from datetime import date
sim = nao = 0
for i in range(0, 7):
    n = int(input(f'Ano de nascimento da {i+1}ª pessoa: '))
    if (date.today().year - n) < 21:
        nao += 1
    elif (date.today().year - n) >= 21:
        sim += 1
print(f'{sim} são maiores de 21 anos.')
print(f'{nao} são menores de 21 anos.')