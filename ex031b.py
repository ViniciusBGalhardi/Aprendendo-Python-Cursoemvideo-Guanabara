d = float(input('Qual a distancia da viajem em Km? '))
preço = d / 2 if d <= 200 else d * 0.45
print(f'Para uma viajem de {d}Km preço da passagem fica R${preço:.2f}.')
