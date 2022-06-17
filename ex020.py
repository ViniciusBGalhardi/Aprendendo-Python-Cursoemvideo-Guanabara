from random import shuffle
a1 = input('Nome do 1° aluno(a): ')
a2 = input('Nome do 2° aluno(a): ')
a3 = input('Nome do 3° aluno(a): ')
a4 = input('Nome do 4° aluno(a): ')
lista = [a1, a2,a3,a4]
shuffle(lista)
print(f'A ordem de apresentação sera: {lista}')