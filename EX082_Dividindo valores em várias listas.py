lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if perg in 'n':
        break
pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Todos os valores digitados: {lista}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')
