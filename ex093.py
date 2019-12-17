print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"CADASTRO DE JOGADOR DE FUTEBOL":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

jogador = dict()
gols = list()
soma = 0

jogador['Nome'] = str(input('Nome do Jogador: '))
numJogos = int(input(f'Quantas partida {jogador["Nome"]} jogou? '))

for i in range(0, numJogos):
    gols.append(int(input(f'Gols na {i+1}ª partida: ')))
    soma = soma + gols[i]
jogador['Gols'] = gols
jogador['Total'] = soma

print(f'\033[1m{"-=" * 40}\033[m')
print(jogador)
print(f'\033[1m{"-=" * 40}\033[m')

for k, v in jogador.items():
    if k == 'Nome':
        print(f'O {k} do jogador é \033[1:32m{v}\033[m')
    elif k == 'Gols':
        print(f'{jogador["Nome"]} fez os {k} \033[1:35m{v}\033[m')
    elif k == 'Total':
        print(f'{jogador["Nome"]} fez um {k} de \033[1:33m{v} gols.\033[m')
print(f'\033[1m{"-=" * 40}\033[m')

aproveitamento = float(soma / numJogos)

print(f'O jogador {jogador["Nome"]} jogou {numJogos} partidas.')
for j in range(0, len(gols)):
    if gols[j] == 0:
        print(f'    => Na \033[1:34m{j + 1}ª partida\033[m, fez \033[1:31mNenhum gol\033[m.')
    elif gols[j] == 1:
        print(f'    => Na \033[1:34m{j + 1}ª partida\033[m, fez \033[1:31m{gols[j]} gol\033[m.')
    else:
        print(f'    => Na \033[1:34m{j+1}ª partida\033[m, fez \033[1:31m{gols[j]} gols\033[m.')

print(f'\033[1m{"-=" * 40}\033[m')
print(f'Foi um total de {soma} gols em {numJogos} partidas.')
print(f'Teve um aproveitamento de \033[1:32m{aproveitamento:.2f} gols por partida\033[m.')
print(f'\033[1m{"-=" * 40}\033[m')
