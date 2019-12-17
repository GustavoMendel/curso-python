print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"CADASTRO DE JOGADOR DE FUTEBOL - v2.0":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

player = dict()
matches = list()
team = list()
status = 'o'
allMatches = allGoals = 0

while status not in 'nN':
    player['Nome'] = str(input('Nome do jogador: '))
    allMatches = int(input(f'Quantas partidas {player["Nome"]} jogou? '))

    for i in range(0, allMatches):
        matches.append(int(input(f'Gols na {i+1}ª partida: ')))
        allGoals = allGoals + matches[i]

    player['Gols'] = matches[:]
    player['Total'] = allGoals

    team.append(player.copy())
    player.clear()
    matches.clear()
    allGoals = 0

    status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')
    while status not in 'nNsS':
        status = input('Deseja continuar? [\033[1:32mS\033[m/\033[1:31mN\033[m] ')
    print(f'\033[1m{"-" * 50}\033[m')

print(f'Nº  Nome         Gols                   Total')
print(f'\033[1m{"-" * 50}\033[m')
for i in range(0, len(team)):
    if i >= 1:
        print()
    print(f'\033[1m{i:<4}\033[m', end='')
    for k, v in team[i].items():
        if k == 'Nome':
            print(f'\033[1:32m{v:<12}\033[m', end='')
        elif k == 'Gols':
            n = 23 - (len(team[i]['Gols'])*3)
            print(f' \033[1m{v}\033[m', ' '*n, end='')
        elif k == 'Total':
            print(f'\033[1:35m{v:<4}\033[m', end='')

print(f'\n\033[1m{"-" * 50}\033[m')
print(f'\033[1:33m[999 para finalizar]\033[m')

option = int(input('Mostrar dados de qual jogador? (Nº) '))

while option != 999:

    while option < 0 or option > len(team)-1:
        print(f'\033[1:31mERRO!\033[m Não existe um jogador com o nº {option}')
        option = int(input('Mostrar dados de qual jogador? (Nº) '))
        if option == 999:
            break
    if option == 999:
        break
    print(f'>> LEVANTAMENTO DO JOGADOR \033[1:32m{team[option]["Nome"]}\033[m')
    for k in range(0, len(team[option]['Gols'])):
        if team[option]["Gols"][k] == 0:
            print(f'    <> No \033[1:34m{k+1}º jogo\033[m fez \033[1:31mNenhum gol\033[m.')
        elif team[option]["Gols"][k] == 1:
            print(f'    <> No \033[1:34m{k+1}º jogo\033[m fez \033[1:31m{team[option]["Gols"][k]} gol\033[m.')
        else:
            print(f'    <> No \033[1:34m{k+1}º jogo\033[m fez \033[1:31m{team[option]["Gols"][k]} gols\033[m.')

    print(f'\033[1m{"-" * 50}\033[m')

    option = int(input('Mostrar dados de qual jogador? (Nº) '))

print(f'\033[1m{"-" * 50}\033[m')
print(f'\033[33m{"< < < < < < < <-- VOLTE SEMPRE! --> > > > > > > >":^50}\033[m')
