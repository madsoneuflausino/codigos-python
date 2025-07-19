sal = float(input('Informe seu salário: R$'))
if sal <= 1250:
    sal = sal + (sal * 0.15)
    print(f'Seu novo salário é {sal:.2f}. você recebeu \033[32m15%\033[m de aumento.') #adição de cores
else:
    sal = sal + (sal * 0.10)
    print(f'Seu novo salário é {sal:.2f}. Você recebeu \033[31m10%\033[m de aumento.') #adição de cores