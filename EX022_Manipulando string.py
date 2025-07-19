'''
nome = str(input('Digite o seu nome: '))
print('Seu nome em maiúsculo: ', nome.upper())
print('Seu nome em minúsculo: ', nome.lower())
n = nome.split()
print(f'Seu primeiro nome tem {len(n[0])} letras.')
n = ''.join(n)
print(f'Seu nome completo tem {len(n)} letras.')
'''

# OUTRA FORMA DE REALIZAR A TAREFA
n = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculo: {}'.format(n.upper()))
print('Seu nome em minúsculo: {}'.format(n.lower()))
print('Seu nome tem {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
