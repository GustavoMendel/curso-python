def fact(number, show=False):
    """
        -> Calculate the factorial of the number --
    :param number: The integer to calculate the factorial of yourself;
    :param show: (optional) boolean value to show or not the calculation;
    :return: The factorial calculation result;
    """
    n = 1
    if not show:
        for c in range(number, 0, -1):
            n = n * c
        print(f'{number}! = \033[1:34m{n}\033[m')
    else:
        for c in range(number, 0, -1):
            n = n * c
            if c == 1:
                print(f'\033[1:31m{c}\033[m ', end='')
            else:
                print(f'\033[1:31m{c}\033[m x', end=' ')
        print(f'= \033[1:34m{n}\033[m')


def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


intro('FUNÇÃO PARA FATORIAL')

line()
shou = 'false'
num = int(input('Digite um número: '))
how = (input('Deseja mostrar a conta? [\033[1:31mFalse\033[m/\033[1:32mTrue\033[m] '))
if how in 'FalsefalseFalsofalsoNãonãoNaonaonegativoNegativo':
    shou = bool(False)
elif how in 'TruetrueSimsimVerdadeiroverdadeiroqueropositivoPositivo':
    shou = bool(True)

fact(num, shou)
line()
