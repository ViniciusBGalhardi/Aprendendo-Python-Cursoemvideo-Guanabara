n = float(input('Quantos reais você tem? R$'))
print(f'Com R${n:.2f} (reais)  você pode comprar: \n'
      f' ${n / 4.46:.2f} (dollares), \n'
      f' €{n / 5.12:.2f} (euros) e \n'
      f' ¥{n / 0.036:.2f} (Iene japones).')
