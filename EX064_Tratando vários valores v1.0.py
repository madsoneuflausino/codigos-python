num = int(input('Digite um número. [999 - para encerrar]. '))
soma = cont = 0
while num != 999:
    soma += num
    num = int(input('Digite um número. [999 - para encerrar]. '))
    cont += 1
print(f'Foram digitados {cont} números. A soma deles é {soma}.')
