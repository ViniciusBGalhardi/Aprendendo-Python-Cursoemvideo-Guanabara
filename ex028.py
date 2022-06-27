from random import randint
from time import sleep
print('=*' * 20)
n = int(input('Adivinhe que numero de 0 a 5 que estou pensando: '))
print('=*' * 20)
c = randint(0, 5)
print('Comparando...')
sleep(2)
print('=*' * 20)
if 0 <= n <=5:
    if n == c:
        print(f'Acertou miseravi!! Era o {c} mesmo, o proprio telepata!!')
        print('=*' * 20)
    else:
        print(f'Não foi dessa vez bicho, era o {c}, voce é um padrão estatistico!')
        print('=*' * 20)
else:
    print('alem de errar nem interpretar sabe!')
    print('=*' * 20)

