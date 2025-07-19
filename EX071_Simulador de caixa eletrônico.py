print('=-'*15)
print('SAQUE')
print('=-'*15)
print('CÉDULAS DE R$50, R$20, R$10, R$1, ')
valor = int(input('Qual o valor do saque? R$'))
c50 = c20 = c10 = c1 = 0
while True:
    if valor >= 50:
        c50 = valor // 50
        valor = valor % 50
        if valor == 0:
            break
    elif 50 > valor >= 20:
        c20 = valor // 20
        valor = valor % 20
        if valor == 0:
            break
    elif 20 > valor >= 10:
        c10 = valor // 10
        valor = valor % 10
        if valor == 0:
            break
    elif valor < 10:
        c1 = valor // 1
        break

print(f'{c50} cédulas de R$50')
print(f'{c20} cédulas de R$20')
print(f'{c10} cédulas de R$10')
print(f'{c1} cédulas de R$1')
