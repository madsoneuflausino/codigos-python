a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print('As retas formam um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('As retas formam um triângulo isósceles.')
    elif a != b and a != c and b != c: #pode ser escrito 'a != b != c != a'
        print('As retas formam um triângulo escaleno. ')
else:
    print('As retas não formam um triângulo.')
