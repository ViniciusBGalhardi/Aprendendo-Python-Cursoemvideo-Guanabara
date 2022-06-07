n = float(input('Quantos reais você tem? R$'))
d = float(input('Digite a cotação do Dollar em Reais: R$'))
e = float(input('Digite a cotação do Euro em Reais: R$'))
y = float(input('Digite a cotação do Iene japones em Reais: R$'))
print(f'Com R${n:.2f} (Reais)  você pode comprar: \n'
      f' ${n / d:.2f} (Dollares), \n'
      f' €{n / e:.2f} (Euros) e \n'
      f' ¥{n / y:.2f} (Iene japones).')
