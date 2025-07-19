lanche = () #inicializando uma tupla
print(type(lanche))
#lanche = ('suco', 'hamburguer', 'pizza', 'pudim') PODEMOS INICIALIZAR COM OU SEM PARENTESES
lanche = 'suco', 'hamburguer', 'pizza', 'pudim'
#INDICES   0           1          2         3

# fatiamento
print(lanche[1])
print(lanche[0:2])
print(lanche[-1])
print(lanche[-2])
#print(lanche[4])  VAI MOSTRAR UMA MENSAGEM DE ERRO INDICE FORA DA FAIXA
print('='*30)
for comida in lanche:
    print(comida)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont} ')
print('='*40)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('='*40)
a = (1, 2, 3)
b = (4, 5, 6, 7)
c = a + b #concatena os valores das tuplas "a" e "b". a + b, nesse caso torna-se diferente de b + a
print(c)
print(c.count(2)) #retorna o número de vezes que aparece a variável informada na tupla.
print(c.index(5)) #retorna o índice do elemento informado na tupla.