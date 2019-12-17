print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"CONTANDO VOGAIS EM POKÉMON":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

poke = ('Abra', 'Kadabra', 'Alakazam',
        'Squirtle', 'Wartotle', 'Blastoise',
        'Charmander', 'Charmeleon', 'Charizard',
        'Bulbasaur', 'Ivysaur', 'Venusaur',
        'Pichu', 'Pikachu', 'Raichu',
        'Milotic', 'Flygon', 'Steelix')

for c in range(0, len(poke)):
    print(f'O Pokémon \033[1:34m{poke[c]:^10}\033[m tem as vogais: ', end='')
    for count in range(0, len(poke[c])):
        letra = poke[c][count].lower()
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            print(f'\033[1:31m{letra:^1}\033[m', end=' ')
    print('')
