import random
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitorias = 0
while True:
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).lower().strip()
    computador = random.randint(1,10)
    soma = num + computador
    if soma % 2 == 0:
        print(f'Você jogou {num} e o computador {computador}. Total de {soma} -> DEU PAR ')
    if soma % 2 != 0:
        print(f'Você jogou {num} e o computador {computador}. Total de {soma} -> DEU ÍMPAR ')
    if escolha in 'Pp' and soma % 2 == 0 or escolha in 'Ii' and soma % 2 != 0:
        print('Você venceu!\nVamos jogar novamente...')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {vitorias} vez(es).')




