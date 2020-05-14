nome = str(input('Digite seu nome completo: '))

print('Muito prazer em te conhecer.')

lista = nome.split()

print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))
