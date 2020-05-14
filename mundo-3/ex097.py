def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def write(txt):
    size = len(txt)
    print(f'\033[1:31m{"~" * (size+4)}\033[m')
    print(f'\033[1:34m  {txt}  \033[m')
    print(f'\033[1:31m{"~" * (size + 4)}\033[m')


intro('UM PRINT ESPECIAL')

status = 'o'

while status not in 'nN':
    txt = str(input('Digite um texto para ser formatado: '))
    write(txt)
    status = str(input('Deseja escrever novamente? [S/N] '))
    while status not in 'NnSs':
        status = str(input('Deseja escrever novamente? [S/N] '))
