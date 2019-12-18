def intro(x):
    print(f'\033[1:33m{"-" * 40:^40}\033[m')
    print(f'\033[1:33m{x:^40}\033[m')
    print(f'\033[1:33m{"-" * 40:^40}\033[m')


def line():
    print(f'\033[1m{"-=" * 25}\033[m')


def player(name, goals):
    print(f'O jogador {name} fez \033[1:32m{goals} gol(s)\033[m no campeonato!')


intro('FICHA DE JOGADOR')

line()

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    player('\033[31m<desconhecido>\033[m', gols)
else:
    nome = str(f'\033[1:34m{nome}\033[m')
    player(nome, gols)

line()
