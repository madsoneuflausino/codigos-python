while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 20)
    if num < 0:
        break
    for i in range(1,10):
        print(f'{num} X {i} = {num * i}')
    print('='*20)
print('FIM')