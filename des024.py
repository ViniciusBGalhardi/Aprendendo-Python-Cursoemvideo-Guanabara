cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.upper()
c = cidade.split()
print('A cidade começa com o nome Santo?', 'SANTO' in c[0])