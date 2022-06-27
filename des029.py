v = float(input('Qual velocidade em Km/h o carro passou pelo radar? '))
print('Sem multa, velocidade permitida.' if v <= 80 else f'Velocidade acima da permitida, multa de R${(v - 80) * 7:.2f}.')