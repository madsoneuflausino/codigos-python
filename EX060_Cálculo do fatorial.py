num = int(input('Digite um número para saber seu fatorial: '))
fat = 1
n = num
while n > 1:
    fat = fat * n
    n = n - 1
print(f'O fatorial de {num} é {fat}...(feito do WHILE)')

f = 1
for i in range(1, num + 1):
    f = f * i
print(f'O fatorial de {num} é {f} ...(feito com FOR)')


