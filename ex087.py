print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"MATRIZ EM PYTHON - v2.0":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor [{i},{j}]: '))
        if matriz[i][j] % 2 == 0:
            soma = soma + matriz[i][j]
        if j == 2:
            soma3 = soma3 + matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]

print(f'\033[1:33m{"-"*40}\033[m')

for i in range(0, 3):
    print(f'{" ":^12}', end='')
    for j in range(0, 3):
        print(f'\033[1:35m[{matriz[i][j]:^3}]', end='')
    print()

print(f'\033[1:33m{"-"*40}\033[m')
print(f'A soma de todos os números pares é: \n'
      f'\033[1:31mSOMA PARES = {soma}\033[m')
print(f'A soma de todos os números da terceira coluna é: \n'
      f'\033[1:34mSOMA COLUNA 3 = {soma3}\033[m')
print(f'O maior valor da segunda linha é: \n'
      f'\033[1:32mMAIOR DA LINHA 2: {maior}\033[m')
print(f'\033[1:33m{"-"*40}\033[m')
