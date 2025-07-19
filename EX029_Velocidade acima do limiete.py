vel = int(input('velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado em R${multa}')
else:
    print('Continue sendo prudente no trânsito.')
