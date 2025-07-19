frase = str(input('Digite uma frase: ')).strip()
frase = frase.split()
frase = ''.join(frase)

# realizando a tarefa usando listas
l1 = list()
l2 = list()
for i in range(0, len(frase)):
    l1.append(frase[i])
for i in range(0, len(frase)):
    l2.append(frase[i])
l2.reverse()
if l1 == l2:
    print('A frase forma um palíndromo.')
else:
    print('A frase não forma um palíndromo.')

# realizando a tarefa sem usar lista
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print(f'{frase} <===> {inverso}')
if frase == inverso:
    print('A frase forma um PALÍNDROMO.')
else:
    print('A frase NÂO forma um PALÍNDROMO.')