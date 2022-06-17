from math import radians, sin, cos, tan
a = float(input('Digite um angulo: '))
ar = radians(a)
sen = sin(ar)
cos = cos(ar)
tag = tan(ar)
print(f'O angulo de {a}° ou {ar:.2f} radianos tem \n'
      f'O seno igual a {sen:.2f} \n'
      f'O cosseno igual a {cos:.2f} \n'
      f'A tangente igual a {tag:.2f}')