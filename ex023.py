n = int(input('Digite um numero de zero a 9999: '))
print(f"""o numero {n} apresenta:
      Unidade = {n%10}
      Desena = {n//10%10}
      Centena = {n//100%10}
      Milhar = {n//100%10}""")
