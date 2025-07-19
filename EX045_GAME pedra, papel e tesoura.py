import random
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
print('GAME: PEDRA, PAPEL E TESOURA')
print('='*35)
print('Escolha um número.\n0 - PEDRA\n1 - PAPEL\n2 - TESOURA')
print('='*35)
n = int(input())
sort = random.randint(0,2)
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ')
sleep(1)

print(f'Você escolheu: {itens[n]}\nO computador escolheu: {itens[sort]}')
if n == sort:
    print('==EMPATE!==')
elif n == 1 and sort == 3 or n == 2 and sort == 1 or n == 3 and sort == 2:
    print('==VOCÊ GANHOU!==')
else:
    print('==VOCÊ PERDEU!==')