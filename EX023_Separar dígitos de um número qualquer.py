#usando a entrada como string
#OBS: dessa forma ocorrerá um erro quando não digitarmos um número de quatro dígitos

num = (input('Digite um número de 0 a 9999: '))
'''print(f'Unidede: {num[-1]}')
print(f'Dezena: {num[-2]}')
print(f'Centena: {num[-3]}')
print(f'Milhar: {num[-4]}')
'''

#OUTRA FORMA DE REALIZAR A TAREFA TRANSFORMANDO A VARIÁVEL EM UM "INT" E TRABALHANDO COM OPERAÇÕES MATEMÁTICAS
#DESTA FORMA NÃO OCORRE ERRO NA EXECUÇÃO
n = int(num)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))