from time import sleep


def intro(x):
    print(f'\033[1:32:40:7m{"~" * 40:^40}')
    print(f'{x:^40}')
    print(f'{"~" * 40:^40}')
    print('\033[m', end='')


def intro2(x):
    print(f'\033[1:34:40:7m{"~" * 40:^40}')
    print(f'{x:^40}')
    print(f'{"~" * 40:^40}')
    print('\033[m', end='')


def intro3(x):
    print(f'\033[1:31:7m{"~" * 40:^40}')
    print(f'{x:^40}')
    print(f'{"~" * 40:^40}')
    print('\033[m', end='')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def pyhelp(function):
    aspas = str("'")
    sleep(1.2)
    manual = f'Acessando o manual do comando {aspas}{function}{aspas}'
    intro2(manual)
    sleep(1.2)
    print(f'\033[1:7m')
    print(help(function))
    print('\033[m', end='')
    sleep(0.7)


while True:
    intro('SISTEMA DE AJUDA PyHELP')
    bib = str(input('Função ou Biblioteca > '))
    if bib.upper() in 'FIM':
        break
    pyhelp(bib)

intro3('FINALIZANDO ... ATÉ LOGO')
