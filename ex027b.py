n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Muito prazem em te conhecer {n}.\n'
      f'O seu primero nome é {nome[0]}\n'
      f'e o seu ultimo é {nome[len(nome) - 1]}.')