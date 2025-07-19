'''
nome = str(input('Qual o seu nome? '))
print('Seu nome é {}!'.format(nome)) #retorna o nome inserido no INPUT
print('Seu nome é {:^20}!'.format(nome)) #retorna o nome inserido no INPUT com 20 caracteres alinhado ao centro
print(f'Seu nome é {nome:^20}!') #retorna o nome inserido no INPUT com 20 caracteres alinhado ao centro
print(f'Seu nome é {nome:=^20}!') #retorna o nome inserido no INPUT com 20 caracteres alinhado ao centro com '=' em volta

print('Seu nome é {:<20}!'.format(nome)) #retorna o nome inserido no INPUT com 20 caracteres alinhado a direita
print(f'Seu nome é {nome:<20}!') #retorna o nome inserido no INPUT com 20 caracteres alinhado a direita

print('Seu nome é {:>20}!'.format(nome)) #retorna o nome inserido no INPUT com 20 caracteres alinhado a esquerda
print(f'Seu nome é {nome:>20}!') #retorna o nome inserido no INPUT com 20 caracteres alinhado a esquerda

print('=||='*15) # Os operadores multiplicam tudo que estiver entre parênteses
'''
# OPERADORES

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2       #soma dos números
sub = n1 - n2     #subtração dos números
m = n1 * n2       #multiplicação entre os números
d = n1 / n2       #divisão entre os números
exp = n1 ** n2    #potenciação entre os números
di = n1 // n2     #divisão inteira entre os números
r = n1 % n2       #resto de divisão entre os números
print('Os números inseridos foram {} e {}'.format(n1,n2))
print('A soma deles é {}, o produto entre eles é {} e a divisão é {:.2f} '.format(s,m,d), end=' ') #o ponto seguido de 2f faz com que retorne a variável com duas casas decimais. o 'end' cancela a quebra de linha, mesmo que tenha outro print
print(f'{n1} elevado a {n2} é {exp}, a divisão inteira de {n1} e {n2} é {di} \n e o resto de divisão entre {n1} e {n2} é {r}') # '\n' quebra a linha

