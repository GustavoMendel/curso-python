nome = input('Digite o nome completo: ')

print('O nome com as letras minúsculas é: {}'.format(nome.lower()))
print('O nome com as letras maiúsculas é: {}'.format(nome.upper()))
numeroEspaco = nome.count(' ')
tamanho = len(nome)
totalLetras = tamanho - numeroEspaco
print('Este nome tem um total de {} letras ao todo'.format(totalLetras))
print('O primeiro nome tem um total de {} letras ao todo'.format(len(nome.split()[0])))
