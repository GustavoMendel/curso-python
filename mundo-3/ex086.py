print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"MATRIZ EM PYTHON":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
i = j = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor [{i},{j}]: '))

print(f'\033[1:33m{"-"*40:^40}\033[m')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
