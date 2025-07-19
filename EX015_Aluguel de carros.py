dias = int(input('Por quantos dias você alugou o carros? '))
km = float(input('Quantos quilômetros você rodou? '))
pagar = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pagar:.2f}')