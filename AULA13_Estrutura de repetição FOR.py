"""
for c in range(1,6):
    print(c)
print('='*5)
for c in range(6, 0, -1): #decrescente
    print(c)
"""
print('='*5)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)