import random
n = random.randint(0,10)
r = int(input('Pensei em um número entre 0 e 10. Que número é esse? '))
cont = 1
while r != n:
    if r < n:
        r = int(input('Você errou! Mais...tente novamente. Que número pensei? '))
    elif r > n:
        r = int(input('Você errou! Menos...tente novamente. Que número pensei? '))
    cont += 1
print(f'Você palpitou {cont} vez(es) para acertar.')