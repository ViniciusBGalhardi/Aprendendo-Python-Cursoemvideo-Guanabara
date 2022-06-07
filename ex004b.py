a = input('Digite algo: ')
print(f'É apenas numero? {a.isnumeric()} \n'
      f'É apenas alfabetico? {a.isalpha()} \n'
      f'É apenas numero e alfabetico? {a.isalnum()} \n'
      f'É um numero decimal? {a.isdecimal()} \n'
      f'É uma sequencia de digitos? {a.isdigit()} \n'
      f'Só tem letras maiusculas? {a.isupper()} \n'
      f'Só tem letras minusculas? {a.islower()} \n'
      f'É imprimivel? {a.isprintable()} \n'
      f'Só tem espaços? {a.isspace()} \n'
      f'Esta capitalisada? {a.istitle()} \n'
      f'É um indicador Python valido? {a.isidentifier()} \n'
      f'Todos caracteres são ASCII? {a.isascii()}')
# ASCII? INDICADOR PYTHON? DECIMAL?
