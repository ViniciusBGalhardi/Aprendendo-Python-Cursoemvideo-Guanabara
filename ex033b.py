n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
if n3 > n2:
    if n2 > n1:
        print(f'{n3} é maior que {n2} que é maior que {n1}.')
    else:
        if n1 < n3:
            print(f'{n3} é maior que {n1} que é maior que {n2}.')
        else:
            print(f'{n1} é maior que {n3} que é maior que {n2}.')
else:
    if n2 < n1:
        print(f'{n1} é maior que {n2} que é maior que {n3}.')
    else:
        if n1 > n3:
            print(f'{n2} é maior que {n1} que é maior que {n3}.')
        else:
            print(f'{n2} é maior que {n3} que é maior que {n1}.')
