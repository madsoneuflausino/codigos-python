lista = []
while True:
    num = (int(input('Digite um número: ')))
    if num in lista:
        print('Valor duplicado. Não vou adicionar.')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso.')
        pergunta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if pergunta in 'N':
            break
lista.sort()
print(f'Você digitou os valores {lista}')