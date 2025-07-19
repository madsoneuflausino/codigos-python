primeiro = int(input('Digite o 1º termo da PA: '))
razão = int(input('Informe a razão da PA: '))
contador = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo}->', end=' ')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? [0]->Encerrar'))
print('FIM')