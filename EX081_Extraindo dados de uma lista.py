lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    perg = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if perg in 'n':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Valores em ordem descrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')