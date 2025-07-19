import random
from time import sleep
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade = int(input('Quantos jogos quer que eu sorteie? '))
jogo = []
jogos = []
num = 0
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = int(random.randint(1, 60))
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    total += 1
print('GERANDO SEUS JOGOS...')
sleep(2)
for i in range(len(jogos)):
    print(f'JOGO {i+1}: {jogos[i]}')
    sleep(2)
print('-=-=-=-= < BOA SORTE! > =-=-=-=-')
