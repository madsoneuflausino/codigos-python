km = float(input('Informe a distância da viagem em Km: '))
if km <= 200:
    vl = km * 0.50
    print(f'O custo da sua viagem é R${vl:.2f}')
else:
    vl = km * 0.45
    print(f'O custo da sua viagem é R${vl:.2f}')