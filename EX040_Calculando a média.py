n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é {media}')
if media < 5:
    print('REPROVADO')
elif 5 < media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
