peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura**2)
print('='*15)
print(f'\033[32mSeu IMC é {imc:.1f}\033[m')
print('='*15)
if imc < 18.5:
    print('\033[34mAbaixo do peso ideal.\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[32mPeso ideal.\033[m')
elif imc >= 25 and imc < 30:
    print('\033[33mSobrepeso.\033[m')
elif 40 >= imc >= 30:
    print('\033[35mObesidade.\033[m')
elif imc > 40:
    print('\033[31mObesidade mórbida.\033[m')