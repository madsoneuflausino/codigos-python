aluno = []
turma = []
while True:
    aluno.append(str(input('Nome: ')).strip().lower())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
print('=-' * 20)
print(f'{"Nº":<1}{"NOME":<6}{"MÉDIA":>10}')
print('-' * 25)
for i in turma:
    media = (i[1] + i[2]) / 2
    print(f'{turma.index(i):<1} {i[0]:<6} {media:>10}')
while True:
    resp = str(input('Quer ver as notas de qual aluno? 999 - encerra ')).strip().lower()
    if resp == '999':
        print('ENCERRANDO O PROGRAMA!')
        break
    else:
        for a in turma:
            if resp == a[0]:
                print(f'As notas de {a[0]} foram {a[1]} e {a[2]}')