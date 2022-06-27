s = float(input('Qual o salario? '))
print(f'O salario com aumento é R${s * 1.1:.2f}' if s > 1250 else f'O salario com aumento é R${s * 1.15}')
