
cidade = str(input('Digite o nome da cidade: '))
nome = cidade.upper().split()
if len(nome[0]) > 5:
    print('Santo não é o primeiro nome da cidade.')
elif 'SANTO' in nome[0]:
    print('O primeiro nome da cidade é Santo.')
else:
    print('Santo não é o primeiro nome da cidade.')

'''
#REALIZANDO A TAREFA SEM USAR "IF"
cid = str(input('Informe a cidade: ')).strip()
print('O nome da cidade começa com Santo? {}'.format(cid[:5].upper() == 'SANTO'))
'''
'''NAS DUAS SOLUÇÕES OCORRE UM ERRO QUANDO DIGITAMOS UM NOME COMO "SANTOS" QUE É DIFERENTE DE "SANTO",
ASSIM O SISTEMA EXECUTA COMO "TRUE". NA SOLUÇÃO COM IF DÁ PRA SOLUCIONAR COLOCANDO OUTRO IF. '''