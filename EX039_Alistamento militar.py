import datetime

nas = int(input('Informe o ano de nascimento: '))
hoje = datetime.date.today()
teste = hoje.year - nas
if teste == 17:
    print('É hora de se alistar!')
elif teste >= 18:
    print('Passou {} ano(s) do tempo de alistamento!'.format(teste - 18))
elif teste < 17:
    print('Ainda não é hora de se alistar! Falta(m) {} ano(s).'.format(17 - teste))
