s = float(input('Qual o salario? '))
ns = s * 1.1 if s > 1250 else s * 1.15
print(f'O salario com aumento é R${ns}.')
