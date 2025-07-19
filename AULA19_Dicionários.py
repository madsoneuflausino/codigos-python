'''
dicio = {}
dicio = {'nome':'Madson', 'idade':38,'sexo': 'masculino'}
print(dicio.values())
print(dicio.keys())
print(dicio.items())

for chave, valor in dicio.items():
    print(f'{chave} --> {valor}')

# PARTE PRÁTICA
pessoas = {'nome': 'Madson', 'idade': 38, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
for chave in pessoas.keys():
    print(chave)
for valor in pessoas.values():
    print(valor)
for c, v in pessoas.items():
    print(f'{c} = {v}')
'''

brasil = list()
estado = {}
for a in range(0, 3):
    estado['UF'] = str(input('Estado: '))
    estado['SIGLA'] = str(input('sigla: '))
    brasil.append(estado.copy())
