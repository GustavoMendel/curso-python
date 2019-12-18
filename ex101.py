def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 20}\033[m')


def voto(ano):
    from datetime import datetime
    anoAtual = datetime.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com \033[1:35m{idade} anos\033[m, seu voto é \033[1:31mNEGADO\033[m.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com \033[1:35m{idade} anos\033[m, seu voto é \033[1:34mOPCIONAL\033[m.'
    else:
        return f'Com \033[1:35m{idade} anos\033[m, seu voto é \033[1:32mOBRIGATÓRIO\033[m.'


intro('FUNÇÕES PARA VOTAÇÃO')

line()
birth = int(input('Ano de nascimento: '))
print(voto(birth))
line()
