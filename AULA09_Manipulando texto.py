# FATIAMENTO DE STRING

frase = 'CURSO EM VIDEO PYTHON'
#  C  U  R  S  O     E  M     V  I  D   E   O       P   Y   T   H   O   N
#  0  1  2  3  4  5  6  7  8  9  10 11  12  13  14  15  16  17  18  19  20
print(frase)
print(frase[10]) #imprime o caractere na posição 10. Lembrando que o índice começa do '0'
print(frase[3:18]) #imprime do índice 3 até o 17, não imprime o caractere na posição 18.
print(frase[9:-1]) #o '-1' indica o último elemento da lista, então irá imprimir até o penúltimo
print(frase[9:-1:2]) # irá imprimir do índice 9 até o penúltimo, de dois em dois elementos.
print(frase[:10]) #omitindo o início irá começar do índice '0'.
print(frase[9:]) #não sabendo o final podesse informar apenas o início e irá percorrer até o final.
print(frase[9::3]) #inicia do 9 e vai até o final de três em três
print(len(frase)) #len mostra o tamanho
print(frase.count('E')) # count mostra a quantidade de vezes que a variável informada aparece. Python distingue maiúscula e minúscula
print(frase.count('E',3,18)) #usa o count para um intervalo pré-definido
print(frase.find('EO')) #encontra a expressão informada dentro da variável
print(frase.find('ANDROID')) #vai retornar -1, pois a string 'android' não está dentro da variável frase.
print('VIDEO' in frase, 'ANDROID' in frase) #retorna True ou False caso seja ou não seja atendida a premissa.

# TRANSFORMAÇÃO
print(frase.replace('PYTHON','JAVA')) #manipula string alterando o valor antigo por um novo.
print(frase.lower()) #coloca toda a string em minúsculo.
print(frase.capitalize()) #só a primeira letra fica em maiúsculo, o resto fica em minúsculo
print(frase.title()) #coloca todas as inicias de palavras em maiúsculo
f = '    APRENDA PYTHON    '
print(f)
print(f.strip()) #remove todos os espaços inúteis dentro da string
print(f.lstrip()) #remove

#DIVISÃO
print(frase.split()) #divide em uma lista, por padrão onde há espaço
print(''.join(f)) #o join junta string

print(type(f))
f = f.split()
print(f)
print(type(f))
f = ' '.join(f)
print(f)
print(type(f))













































































































































































































































































