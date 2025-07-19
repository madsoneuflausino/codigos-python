nome = str(input('Qual é seu nome: '))
if nome.upper() == 'MADSON': #uma estrutura apenas com 'if' é chamada simples
    print('Seu nome é diferente, {}.'.format(nome))
elif nome.upper() == 'JOÃO':  #estruturas com 'elif' são chamadas aninhadas
    print('Seu nome é bem comum.')
else:
    print('Seu nome é bonito.')
