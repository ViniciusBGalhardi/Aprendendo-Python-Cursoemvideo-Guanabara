frase = str(input('Digite uma frase: ')).upper()
print('A frase apresenta', frase.count('A'),'letras "A"')
print('"A" aparece pela primeira vez na posição {} ou seja o {}º caracter'.format(frase.find('A'),frase.find('A') + 1))
print('"A" aparece pela ultima vez na posição {} ou seja o {}º caracter'.format(frase.rfind('A'), frase.rfind('A') + 1))
