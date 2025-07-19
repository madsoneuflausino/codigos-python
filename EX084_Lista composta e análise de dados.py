dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input(f'Informe o peso de {dados[0]}: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'({i[0]})=', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'({i[0]})', end=' ')