nome = str(input('Digite seu nome: '))
'''
busca = nome.upper()
if 'SILVA' in busca:
    print('Você tem "silva" em seu nome.')
else:
    print(f'Você não tem "Silva" em seu nome')
'''
#RESOLVENDO SEM IF E APENAS MOSTRANDO TRUE OU FALSE
print('Tem "SILVA" no nome? {}'.format('SILVA' in nome.upper()))