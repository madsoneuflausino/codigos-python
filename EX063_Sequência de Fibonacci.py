print('SEQUENCIA DE FIBONACCI')
print('='*35)
n = int(input('Quantos termos você quer mostrar? '))
cont = 1
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' - {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1


