ano = int(input('Digite um ano para saber se é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é bissexto.')
elif ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
