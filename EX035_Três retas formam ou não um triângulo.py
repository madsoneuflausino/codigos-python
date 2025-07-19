a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
