d = float(input('Qual a distancia da viajem em Km? '))
print(f'O preço da passagem fica R${d / 2:.2f}.' if d <= 200 else f'O preço da passagem fica R${d * 0.45:.2f}.')
