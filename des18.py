import math
a = float(input('Digite um angulo: '))
ar = math.radians(a)
sen = math.sin(ar)
cos = math.cos(ar)
tag = math.tan(ar)
print(f'O angulo de {a}° tem \n'
      f'O seno igual a {sen:.2f} \n'
      f'O cosseno igual a {cos:.2f} \n'
      f'A tangente igual a {tag:.2f}')