somaIdade = 0
mediaIdade = 0
homemMaisVelho = ''
idadeMaisVelho = 0
totMulheres = 0
for p in range(1,5):
    print(f'===={p}ª PESSOA ====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if sexo in 'Mm' and p == 1:
        homemMaisVelho = nome
        idadeMaisVelho = idade
    if sexo in 'Mm' and idade > idadeMaisVelho:
        homemMaisVelho = nome
        idadeMaisVelho = idade
    if sexo in 'Ff' and idade < 20:
        totMulheres += 1
mediaIdade = somaIdade / 4
print(f'A média de idade é: {mediaIdade} anos.')
print(f'O homem mais velho é: {homemMaisVelho}.')
print(f'O total de mulheres menores de 20 anos é: {totMulheres}')

# solução utilizando listas
'''
listaNome = list()
listaIdade = list()
listaSexo = list()
for i in range(0, 4):
    nome = str(input('Digite o nome: '))
    listaNome.append(nome)
    idade = int(input('Digite a idade: '))
    listaIdade.append(idade)
    sexo = str(input('Sexo M ou F: '))
    listaSexo.append(sexo)
    print('='*20)

#calculo da média das idades
s = 0
for a in range(0, 4):
    s += listaIdade[a]
print(f'A média das idades é: {s / 4} anos.')

#checando o printando o nome do mais velho
maisVelho = listaIdade.index(max(listaIdade))
if maisVelho == 0:
    print(f'O mais velho é {listaNome[0]}')
if maisVelho == 1:
    print(f'O mais velho é {listaNome[1]}')
if maisVelho == 2:
    print(f'O mais velho é {listaNome[2]}')
if maisVelho == 3:
    print(f'O mais velho é {listaNome[3]}')

#mulheres com menos de 20 anos
soma = 0
for c in range(0, 4):
    if listaIdade[c] < 20:
        if listaSexo[c] == 'F':
            soma += 1
print(f'{soma} mulheres tem menos de 20 anos')
'''