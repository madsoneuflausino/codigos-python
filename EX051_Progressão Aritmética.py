p1 = int(input('1º termo da PA: '))
r = int(input('Razão da PA: '))
l = list()
l.append(p1)
for i in range(0, 9):
    t = l[i] + r
    l.append(t)
print(l)

# realizando a tarefa sem usar lista
decimo = p1 + (10 - 1) * r # fórmula para calcular o enésimo termo de uma PA
for i in range(p1, decimo + r, r):
    print(f'{i}', end='->')
print('FIM')