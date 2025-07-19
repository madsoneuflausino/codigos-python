import random

num = int(input('Pensei em um número entre 0 e 5. Que número é esse?: '))
n = random.randint(0,5)
if num == n:
    print('Parabéns, você acertou o número aleatório gerado.')
else:
    print('Que pena, não foi dessa vez.')
print(f'O número gerado foi {n}')