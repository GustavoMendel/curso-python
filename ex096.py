def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def area(c, l):
    result = c * l
    print(f'Um terreno com as dimensões: '
          f'\nComprimento = \033[1:34m{c} m\033[m'
          f'\nLargura = \033[1:31m{l} m\033[m'
          f'\nEntão sua área é: ...'
          f'\n\033[1:32mÁrea = {result:.1f} m²\033[m')


intro('CALCULANDO ÁREAS COM FUNÇÕES')

a = float(input('Comprimento (m): '))
b = float(input('Largura (m): '))

area(a, b)
