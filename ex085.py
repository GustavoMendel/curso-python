print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"LISTAS COM PARES E ÍMPARES":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

num = [[], []]

for c in range(0, 7):
    aux = int(input(f'Digite o {c+1}º valor: '))
    if aux % 2 == 0:
        num[0].append(aux)
    else:
        num[1].append(aux)
num[0].sort()
num[1].sort()

print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'Os números pares digitados foram: \033[1:31m{num[0]}\033[m')
print(f'Os números ímpares digitados foram: \033[1:34m{num[1]}\033[m')
