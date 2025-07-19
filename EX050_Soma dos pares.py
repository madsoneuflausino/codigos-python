s = 0
for i in range(0,6):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares é: {s}')