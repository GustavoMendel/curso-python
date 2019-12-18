def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def readInt(value):
    number = input(value)
    while number.isnumeric() is False:
        print('\033[1:31mERRO! Digite um número inteiro.\033[m')
        number = input('Digite um número: ')
    return number


intro('VALIDANDO ENTRADA DE DADOS')

line()
n = readInt('Digite um número: ')
print(f'\033[1:32mSUCESSO!\033[m Você digitou um número inteiro {n}.')
line()
