r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 <= r3:
    print('Esses valores não formam um triangulo.')
else:
    if r2 + r3 <= r1:
        print('Esses valores não formam um triangulo.')
    else:
        if r3 + r1 <= r2:
            print('Esses valores não formam um triangulo.')
        else:
            print('Esses valores podem formar um triangulo.')

