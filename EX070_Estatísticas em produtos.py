print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
total = maiormil = maisbarato = 0
nome = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    perg = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    while perg not in 'sn':
        perg = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    total += preco
    if preco > 1000:
        maiormil += 1
    if maisbarato == 0 or maisbarato > preco:
        maisbarato = preco
        nome = produto
    if perg in 'n':
        break
print(f'O total da compra foi de R${total}')
print(f'Temos {maiormil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi o(a) {nome} que custa R${maisbarato}')
