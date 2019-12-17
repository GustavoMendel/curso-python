from time import sleep
from sys import exit
from random import randint

print('\033[1:31m-=-\033[m' * 13)
print('\033[1m      GAME: Pedra, Papel, Tesoura.   \033[m')
print('\033[1:31m-=-\033[m' * 13)

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
statusJ = -1
statusCP = -1

computador = randint(0, 2)
if computador == 0:
    statusCP = jogadas[0]
elif computador == 1:
    statusCP = jogadas[1]
elif computador == 2:
    statusCP = jogadas[2]
sleep(1)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Pedra, papel, tesoura? '))
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ...')
if jogador == 0:
    statusJ = jogadas[0]
elif jogador == 1:
    statusJ = jogadas[1]
elif jogador == 2:
    statusJ = jogadas[2]

if 0 > jogador > 2:
    sleep(1)
    print('\033[1:31m... JOGADA INVÁLIDA ... \033[m')
    exit()
sleep(2)
print('\033[1:31m-=-\033[m' * 10)
print('O Jogador jogou {}'.format(statusJ))
print('O computador jogou {}'.format(statusCP))
print('\033[1:31m-=-\033[m' * 10)

sleep(3)

if computador == jogador:
    print('\033[1:33mEMPATE!!\033[m')

status = -1

if computador == 0 and jogador == 1:
    status = 1
elif computador == 0 and jogador == 2:
    status = 0
elif computador == 1 and jogador == 0:
    status = 0
elif computador == 1 and jogador == 2:
    status = 1
elif computador == 2 and jogador == 0:
    status = 1
elif computador == 2 and jogador == 1:
    status = 0

if status == 0:
    print('\033[1:31mVOCÊ PERDEU !!\033[m')
elif status == 1:
    print('\033[1:32mVOCÊ GANHOU !!\033[m')
