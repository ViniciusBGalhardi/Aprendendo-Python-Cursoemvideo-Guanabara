n = float(input('Digite um valor em metros: '))
print(f'{n} metros é equivalente a \n'
      f' {n * 1000:.2f} milimetros, \n'
      f' {n * 100:.2f} centimetros, \n '
      f'{n * 10:.2f} decimetros,\n '
      f'{n / 10:.6f} decametros, \n '
      f'{n / 100:.6f} hectômetro e \n '
      f'{n / 1000:.6f} Kilometros.')
