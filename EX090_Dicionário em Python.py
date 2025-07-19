dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Media'] = float(input(f'Média de {dicionario["Nome"]}: '))

if dicionario['Media'] >= 7:
    dicionario['Situação'] = '\033[32mAPROVADO\033[m'
elif 5 <= dicionario['Media'] < 7:
    dicionario['Situação'] = '\033[34mRECUPERAÇÃO\033[m'
else:
    dicionario['Situação'] = '\033[31mREPROVADO\033[m'
print('=-' * 20)
for c, v in dicionario.items():
    print(f'--> {c} é igual a {v}')