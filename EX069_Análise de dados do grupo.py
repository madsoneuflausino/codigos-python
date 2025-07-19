homens = mulheres = maioridade = 0
while True:
    sexo = str(input('Informe o sexo: [M/F} ')).lower().strip()
    while sexo not in 'mf':
        sexo = str(input('Informe o sexo: [M/F} ')).lower().strip()
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maioridade += 1
    if sexo in 'm':
        homens += 1
    if sexo in 'f' and idade < 20:
        mulheres += 1
    print('=-'*25)
    perg = str(input('Quer continuar? [S/N] ')).lower().strip()
    while perg not in 'sn':
        perg = str(input('Quer continuar? [S/N] ')).lower().strip()
    if perg in 'n':
        break
print('=-'*25)
print(f'{maioridade} pessoas tem mais de 18 anos')
print(f'Foram cadastrados {homens} homens.')
print(f'Temos {mulheres} mulheres com menos de 20 anos.')
