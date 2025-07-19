print('='*35)
print(f'{"PROGRAMA SIMULADOR DE EMPRÉSTIMO":>33}')
print('='*35)
vCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Informe o valor de seu salário: R$'))
tempo = int(input('Em quantos anos deseja pagar? '))
parcela = vCasa / (tempo * 12)
if parcela > (salario * 0.3):
    print('Empréstimo negado. O valor da parcela excede seu limite')
    print(f'Seu limite de parcela para o salário informado é: R${salario * 0.3:.2f}\nO valor da parcela ficou R${parcela:.2f} ')
else:
    print(f'Empréstimo concedido. O valor da parcela é R${parcela:.2f}')