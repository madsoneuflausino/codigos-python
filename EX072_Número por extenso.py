numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = input('Digite um número entre 0 e 20: ')
    if n.isnumeric() == True:
        n = int(n)
        if 0 < n < 20:
            break
print(f'Você digitou {numeros[n]}.')
