from time import sleep
from random import randint

print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"JOGO DE DADOS EM PYTHON":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

dado = dict()
dado1 = dict()
dado['Jogador1'] = randint(1, 6)
dado['Jogador2'] = randint(1, 6)
dado['Jogador3'] = randint(1, 6)
dado['Jogador4'] = randint(1, 6)

print('Valores sorteados: ')

for k, v in dado.items():
    sleep(1)
    print(f'    O {k} tirou {v}')

print('Ranking dos jogadores: ')

valores = list()
jogadores = list()
aux = 0

for i in dado.values():
    valores.append(i)

for i in dado.keys():
    jogadores.append(i)

for i in range(0, len(valores)-1):
    for j in range(i+1, len(valores)):
        if valores[j] > valores[i]:
            aux = valores[j]
            valores[j] = valores[i]
            valores[i] = aux
            aux = jogadores[j]
            jogadores[j] = jogadores[i]
            jogadores[i] = aux

for i in range(0, len(valores)):
    dado1[f'{jogadores[i]}'] = f'{valores[i]}'

j = 1
for k, v in dado1.items():
    if j == 1:
        print(f'\033[1:32m    {j}º lugar: {k} com {v}\033[m')
    elif j == len(valores):
        print(f'\033[1:31m    {j}º lugar: {k} com {v}\033[m')
    else:
        print(f'    {j}º lugar: {k} com {v}')
    sleep(1)
    j = j + 1
