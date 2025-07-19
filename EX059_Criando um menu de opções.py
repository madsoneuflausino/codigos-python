n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
r = 0
while r != 5:
    r = int(input('''
    ===== MENU =====
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
>>>>Qual a sua opção? '''))
    if r == 1:
        print(f'A soma dos números é {n1 + n2}')
    if r == 2:
        print(f'O produto dos números é {n1 * n2}')
    if r == 3:
        if n1 > n2:
            print(f'{n1} é o maior número.')
        else:
            print(f'{n2} é o maior número.')
    if r == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
print('=== FIM ===')