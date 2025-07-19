p = int(input('1º termo da PA: '))
r = int(input('Razão da PA: '))
n = 1
while n <= 10:
    print(f'{p} ->', end=' ')
    p += r
    n += 1
print('FIM')