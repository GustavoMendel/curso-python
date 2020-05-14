from time import sleep
from random import randint

print(f'\033[1:33m{"-"*40:^40}\033[m')
print(f'\033[1:33m{"PALPITES PARA A MEGA SENA":^40}\033[m')
print(f'\033[1:33m{"-"*40:^40}\033[m')

jogo = list()
aux = list()

num = int(input('Quantos jogos deseja fazer? '))

for c in range(0, num):
    cont = 0
    while True:
        x = randint(1, 60)
        if x not in aux:
            aux.append(x)
            cont = cont + 1
        if cont >= 6:
            break
    aux.sort()
    jogo.append(aux[:])
    aux.clear()

print(f'\033[1:36m{"-"*40}\033[m')
print(f'\033[1m{"SORTEANDO ":>20}{num}{" JOGOS"}\033[m')
print(f'\033[1:36m{"-"*40}\033[m')

for c in range(0, num):
    sleep(1)
    print(f'Jogo {c+1}: {jogo[c]}')
sleep(1)
print(f'{"< BOA SORTE! >":-^40}')
