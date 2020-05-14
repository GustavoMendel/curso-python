x = input('Digite algo: ')

print('O tipo primitivo é {}'.format(type(x)))
print('Ele tem valor numérico? {}'.format(x.isnumeric()))
print('Ele tem característica de ser alfabeto? {}'.format(x.isalpha()))
print('Ele tem característica de ser alfanumérico? {}'.format(x.isalnum()))
print('Ele é um espaço? {}'.format(x.isspace()))
print('Ele tem todos os caracteres maiúsculos? {}'.format(x.isupper()))
print('Ele tem todos os caracteres minúsculos? {}'.format(x.islower()))
