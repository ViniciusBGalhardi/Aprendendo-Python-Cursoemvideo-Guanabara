n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n1 > n2 and n2 > n3:
    print(f'{n1} > {n2} > {n3}')
if n1 > n3 and n3 > n2:
    print(f'{n1} > {n3} > {n2}')
if n2 > n1 and n1 > n3:
    print(f'{n2} > {n1} > {n3}')
if n2 > n3 and n3 > n1:
    print(f'{n2} > {n3} > {n1}')
if n3 > n1 and n1 > n2:
    print(f'{n3} > {n1} > {n2}')
if n3 > n2 and n2 > n1:
    print(f'{n3} > {n2} > {n1}')

