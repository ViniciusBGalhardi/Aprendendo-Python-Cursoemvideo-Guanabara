n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
if n2 > n3 and n2 > n1:
    maior = n2
menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
if n2 < n3 and n2 < n1:
    menor = n2
print(f'O menor é o {menor} e o maior é o {maior}.')
