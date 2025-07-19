dados = []
pessoa = []
while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input(f'Informe a idade de {dados[0]}: ')))
    pessoa.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
for p in pessoa:
    print(f'Nome: {p[0]}   Idade: {p[1]} anos')