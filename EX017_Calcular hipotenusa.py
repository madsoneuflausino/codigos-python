from math import *
co = float(input('Digite o valor do cateto oposto. '))
ca = float(input('Digite o valor do cateto adjacente. '))
h =  hypot(co,ca)
print(f'A hipotenusa do triângulo é {round(h,2)}') #a função round arredonda o número para a quantidade de casas decimais informadas após a vírgula