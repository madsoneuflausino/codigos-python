per = 's'
soma = cont = 0
while per in 's':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    per = str(input('Deseja continuar : [S] ou [N] '.lower()))
media = soma / cont
print(f'A média dos números digitados é {media:.1f}')
print(f'O maior valor informado foi {maior} e o menor valor {menor}.')

