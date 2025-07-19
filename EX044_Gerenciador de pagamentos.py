vProd = float(input('Informe o valor do produto: R$'))
print('='*20)
print("FORMAS DE PAGAMENTO:\n1 - À VISTA\n2 - 1X NO CARTÃO\n3 - 2X NO CARTÃO\n4 - 3X NO CARTÃO")
print('='*20)
f = int(input())
if f == 1:
    vProd = vProd - (vProd * 0.10)
if f == 2:
    vProd = vProd - (vProd * 0.05)
if f == 3:
    vProd = vProd
if f == 4:
    vProd = vProd + (vProd * 0.20)
print(f'Valor a pagar: R${vProd:.2f}')