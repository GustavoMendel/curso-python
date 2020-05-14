from math import pow, sqrt

x1 = float(input('Valor do cateto oposto: '))
x2 = float(input('Valor do cateto adjacente: '))

resultado = pow(x1, 2) + pow(x2, 2)
raiz = sqrt(resultado)

print('A hipotenusa tem comprimento {:.2f}'.format(raiz))
