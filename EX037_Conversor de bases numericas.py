n = int(input('Informe um número qualquer: '))
print('Para qual base deseja converter o número?  ')
res = int(input('Digite:\n\033[032m1\033[m para binário\n\033[032m2\033[m para octal\n\033[032m3\033[m para hexadecimal\n'))

l = list()

#Será executado se optou pela conversão em binário
if res == 1:
    q = n // 2
    r = n % 2
    l.append(r)
    while q >= 2:
        r = q % 2
        q = q // 2
        l.append(r)
        if q < 2:
            l.append(q)

#Será executado se optou pela conversão em octal
if res == 2:
    q = n // 8
    r = n % 8
    if q > 8:
        l.append(r)
        while q >= 8:
            r = q % 8
            q = q // 8
            l.append(r)
            if q < 8:
                l.append(q)
    else:
        l.append(r)
        l.append(q)

#Será executado se optou pela conversão em hexadecimal
if res == 3:
    q = n // 16
    r = n % 16
    if q > 16:
        if r == 10:
            r = 'a'
        if r == 11:
            r = 'b'
        if r == 12:
            r = 'c'
        if r == 13:
            r = 'd'
        if r == 14:
            r = 'e'
        if r == 15:
            r = 'f'
        l.append(r)
        while q >= 16:
            r = q % 16
            q = q // 16
            if r == 10:
                r = 'a'
            if r == 11:
                r = 'b'
            if r == 12:
                r = 'c'
            if r == 13:
                r = 'd'
            if r == 14:
                r = 'e'
            if r == 15:
                r = 'f'
            l.append(r)
            if q < 16:
                l.append(q)
    else:
        if r == 10:
            r = 'a'
        if r == 11:
            r = 'b'
        if r == 12:
            r = 'c'
        if r == 13:
            r = 'd'
        if r == 14:
            r = 'e'
        if r == 15:
            r = 'f'
        l.append(r)
        if q != 0:
            l.append(q)
           
l.reverse()
for i in l:
    print(i,end='')

f'''
# está opção usa uma função interna do Python
print(f'O número {n} em binário é: {bin(n)}')
print(f'O número {n} em octal é: {oct(n)}')
print(f'O número {n} em hexadecimal é: {hex(n)}')
'''