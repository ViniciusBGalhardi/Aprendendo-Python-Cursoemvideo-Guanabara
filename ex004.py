a = input('Digite algo: ')
print(f'O tipo primitivo é{type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numero? {a.isnumeric()}')
print(f'É afabetico? {a.isalpha()}')
print(f'É afanumerico? {a.isalnum()}')
print(f'Esta em maiuscula? {a.isupper()}')
print(f'Esta em minuscula? {a.islower()}')
print(f'Esta capitalizada? {a.istitle()}')


