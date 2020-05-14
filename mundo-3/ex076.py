print('-' * 40)
print(f'\033[1:34m{"LISTAGEM DE COMPRAS":^40}\033[m')
print('-' * 40)

compras = ('Pokeball', 10,
           'Greatball', 25.5,
           'Ultraball', 59.99,
           'Diveball', 15.59,
           'DuskBall', 24.89,
           'Fire Stone', 80,
           'Water Stone', 85,
           'Leaf Stone', 82.79,
           'Thunder Stone', 87.39,
           'Dusk Stone', 80,
           'Dragon Stone', 200,
           'Sun Stone', 300,
           'Fairy Stone', 999.99)

for c in range(0, len(compras), 2):
    tamanho = len(compras[c])
    n = 30 - tamanho

    print(f'\033[1m{compras[c]}\033[m', end='')
    print('.' * n, end='')
    print(f'\033[1:32mR$ {compras[c + 1]:.2f}\033[m')
