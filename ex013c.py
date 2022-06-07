p = float(input('Digite o preço do produto: R$'))
d = float(input('Digite a porcentagem do desconto a vista: '))
a = float(input('Digite a porcentagem do aumento da parcela: '))
print(f'O preço a vista com {d:.2f}% de desconto é R${(p*(100 - d))/100:.2f} \n'
      f'O preço final com aumento de {a:.2f}% da parcela é R${(p*(100 + a))/100:.2f}')
