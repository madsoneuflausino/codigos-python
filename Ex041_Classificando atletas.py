import datetime

nasc = int(input('Informe o ano de nascimento: '))
hoje = datetime.date.today()
idade = hoje.year - nasc
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <=14: #forma tradicional
    print('Categoria Infantil')
elif 19 >= idade > 14: #forma convencional da matemática
    print('Categora Junior')
elif idade <= 20: #forma reduzida aceita pelo Python
    print('Categoria Senior')
elif idade > 20:
    print('Categoria Master')